# The MIT License - EVE Corporation Management
# 
# Copyright (c) 2010 Robin Jarry
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import re

__date__ = "2011-03-08"
__author__ = "diabeteman"


import binascii
import httplib as http

from django.template.context import RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser, Group
from django.http import HttpResponse
from django.conf import settings

from ecm.data.common.models import Url
from ecm.data.roles.models import CharacterOwnership

#------------------------------------------------------------------------------
def basic_auth_required(username=None):
    def decorator(view_function):
        def _wrapped_view(request, *args, **kwargs):
            if request.user in (False, None, AnonymousUser()):
                auth_string = request.META.get('HTTP_AUTHORIZATION', None)
            
                if not auth_string:
                    return HttpResponse(status=http.UNAUTHORIZED)
                    
                try:
                    (auth_method, auth_credentials) = auth_string.split(" ", 1)
            
                    if not auth_method.lower() == 'basic':
                        return HttpResponse(status=http.UNAUTHORIZED)
            
                    auth_credentials = auth_credentials.strip().decode('base64')
                    user, pwd = auth_credentials.split(':', 1)
                except (ValueError, binascii.Error):
                    return HttpResponse(status=http.UNAUTHORIZED)
            
                request.user = authenticate(username=user, password=pwd) or AnonymousUser()
            
            if not request.user in (False, None, AnonymousUser()):
                if username and not (request.user.username == username
                                  or request.user.is_superuser):
                    return HttpResponse(status=http.FORBIDDEN)
                else:
                    return view_function(request, *args, **kwargs)
            else:
                return HttpResponse(status=http.UNAUTHORIZED)
            
        return _wrapped_view
    
    return decorator


#------------------------------------------------------------------------------
def check_user_access():
    """
    Decorator for views that matches the asked URL against those configured in the database
    
    if the user is not logged in, redirect him/her to the login page
    if the user is allowed to consult the URL, then return to the view function
    if the page is the details of a member, check if the user owns the character. 
       If so, allow the user to consult the page anyway
    if the user is not allowed, issue a "forbidden" page
    """
    def decorator(view_function):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated():
                access_ok = False
                for url in Url.objects.all():
                    url_re = re.compile(url.pattern)
                    if url_re.match(request.get_full_path()):
                        access_ok = set(url.groups.all()).intersection(set(request.user.groups.all()))
                        break
                if not access_ok:
                    try:
                        url_re = re.compile("^/members/\d+.*$")
                        if url_re.match(request.get_full_path()):
                            characterID = int(args[0])
                            user = CharacterOwnership.objects.get(character=characterID).owner
                            access_ok = (user == request.user)
                    except:
                        pass
                if request.user.is_superuser or access_ok:
                    return view_function(request, *args, **kwargs)
                else:
                    return forbidden(request)
            else:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.get_full_path())
        return _wrapped_view
    return decorator

#------------------------------------------------------------------------------
def forbidden(request):
    response = render(request, 'auth/forbidden.html',
                      {'request_path' : request.get_full_path()},
                      context_instance=RequestContext(request))
    response.status_code = http.FORBIDDEN
    return response

#------------------------------------------------------------------------------
try:
    g = Group.objects.get(id=settings.DIRECTOR_GROUP_ID)
    if g.name != settings.DIRECTOR_GROUP_NAME:
        g.name = settings.DIRECTOR_GROUP_NAME
        g.save()
except Group.DoesNotExist:
    Group.objects.create(id=settings.DIRECTOR_GROUP_ID, 
                         name=settings.DIRECTOR_GROUP_NAME)