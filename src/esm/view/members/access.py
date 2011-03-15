'''
This file is part of ESM

Created on 13 mars 2011
@author: diabeteman
'''
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from ism.view import getScanDate
from ism.data.roles.models import TitleMembership, RoleMemberDiff, TitleMemberDiff
from django.shortcuts import render_to_response
from ism.core import utils
from ism import settings
from django.template.context import RequestContext
import json
from django.http import HttpResponse
from ism.core.utils import print_time_min




#------------------------------------------------------------------------------
@user_passes_test(lambda user: utils.isDirector(user), login_url=settings.LOGIN_URL)
@cache_page(60 * 60 * 15) # 1 hour cache
@csrf_protect
def access_changes(request):
    data = {
        'scan_date' : getScanDate(TitleMembership.__name__) 
    }
    return render_to_response("members/access_changes.html", data, context_instance=RequestContext(request))


#------------------------------------------------------------------------------
@user_passes_test(lambda user: utils.isDirector(user), login_url=settings.LOGIN_URL)
@cache_page(60 * 60 * 15) # 1 hour cache
@csrf_protect
def access_changes_data(request):
    iDisplayStart = int(request.GET["iDisplayStart"])
    iDisplayLength = int(request.GET["iDisplayLength"])
    sEcho = int(request.GET["sEcho"])

    count, changes = getAccessChanges(first_id=iDisplayStart, 
                                      last_id=iDisplayStart + iDisplayLength - 1)
    json_data = {
        "sEcho" : sEcho,
        "iTotalRecords" : count,
        "iTotalDisplayRecords" : count,
        "aaData" : changes
    }
    
    return HttpResponse(json.dumps(json_data))



#------------------------------------------------------------------------------
def getAccessChanges(first_id, last_id):
    
    roles = RoleMemberDiff.objects.all().order_by("-date")
    titles = TitleMemberDiff.objects.all().order_by("-date")
    
    count = roles.count() + titles.count()
    
    changes = utils.merge_lists(roles, titles, ascending=False, attribute="date")
    changes = changes[first_id:last_id]
    
    change_list = []
    for c in changes:
        try:
            access = '<a href="/titles/%d" class="title">%s</a>' % (c.title_id, unicode(c.title)) 
        except AttributeError:
            role_type_id = c.role.roleType.id
            role_id = c.role.roleID
            access = '<a href="/roles/%d/%d" class="role">%s</a>' % (role_type_id, role_id, unicode(c.role))
        
        try:
            member_url = '<a href="/members/%d">%s</a>' % (c.member.characterID, c.member.name)
        except:
            member_url = '<a href="/members/%d">%s</a>' % (c.member_id, "???")
        
        change = [
            c.new,
            member_url,
            access,
            print_time_min(c.date)
        ]

        change_list.append(change)
    
    return count, change_list