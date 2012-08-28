# Copyright (c) 2010-2012 Robin Jarry
#
# This file is part of EVE Corporation Management.
#
# EVE Corporation Management is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# EVE Corporation Management is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

__date__ = '2012 3 16'
__author__ = 'diabeteman'

from ecm.apps.hr.models.member import Skill

#-----------------------------------------------------------------------------
def get_character_skills(member, sheet):
    skills = []
    for skill in sheet.skills:
        
        try:
            db_skill = member.skills.get(eve_type_id=skill.typeID)
        except Skill.DoesNotExist:
            db_skill = Skill(character=member, eve_type_id=skill.typeID)
        
        db_skill.skillpoints = skill.skillpoints
        db_skill.level = skill.level
        skills.append(db_skill)
    
    return skills

#-----------------------------------------------------------------------------
def set_extended_char_attributes(member, sheet):
    member.DoB = sheet.DoB
    member.race = sheet.race
    member.bloodLine = sheet.bloodLine
    member.ancestry = sheet.ancestry
    member.gender = sheet.gender
    member.cloneName = sheet.cloneName
    member.cloneSkillPoints = sheet.cloneSkillPoints
    member.balance = sheet.balance
    try:
        member.memoryBonusName = sheet.memoryBonusName
        member.memoryBonusValue = sheet.memoryBonusValue
    except AttributeError:
        member.memoryBonusName = None
        member.memoryBonusValue = 0
    try:
        member.intelligenceBonusName = sheet.intelligenceBonusName
        member.intelligenceBonusValue = sheet.intelligenceBonusValue
    except AttributeError:
        member.intelligenceBonusName = None
        member.intelligenceBonusValue = 0
    try:
        member.charismaBonusName = sheet.charismaBonusName
        member.charismaBonusValue = sheet.charismaBonusValue
    except AttributeError:
        member.charismaBonusName = None
        member.charismaBonusValue = 0
    try:
        member.willpowerBonusName = sheet.willpowerBonusName
        member.willpowerBonusValue = sheet.willpowerBonusValue
    except AttributeError:
        member.willpowerBonusName = None
        member.willpowerBonusValue = 0
    try:
        member.perceptionBonusName = sheet.perceptionBonusName
        member.perceptionBonusValue = sheet.perceptionBonusValue
    except AttributeError:
        member.perceptionBonusName = None
        member.perceptionBonusValue = 0
    member.intelligence = sheet.attributes.intelligence
    member.memory = sheet.attributes.memory
    member.charisma = sheet.attributes.charisma
    member.perception = sheet.attributes.perception
    member.willpower = sheet.attributes.willpower