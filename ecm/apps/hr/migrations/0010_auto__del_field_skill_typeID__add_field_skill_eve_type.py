#@PydevCodeAnalysisIgnore
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Skill.typeID'
        db.delete_column('hr_skill', 'typeID')

        # Adding field 'Skill.eve_type'
        db.add_column('hr_skill', 'eve_type',
                      self.gf('ecm.lib.softfk.SoftForeignKey')(to=orm['eve.Type'], null=True, blank=True),
                      keep_default=False)

        if not db.dry_run:
            orm.Skill.objects.all().delete()

    def backwards(self, orm):
        # Adding field 'Skill.typeID'
        db.add_column('hr_skill', 'typeID',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Skill.eve_type'
        db.delete_column('hr_skill', 'eve_type_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'corp.corporation': {
            'Meta': {'object_name': 'Corporation'},
            'allianceID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'allianceName': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'allianceTicker': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'ceoID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ceoName': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'corporationID': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'corporationName': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ecm_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'is_my_corp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_trusted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key_fingerprint': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'memberLimit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'private_key': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'public_key': ('django.db.models.fields.TextField', [], {'unique': 'True', 'blank': 'True'}),
            'stationID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stationName': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'taxRate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        'corp.hangar': {
            'Meta': {'ordering': "['hangarID']", 'object_name': 'Hangar'},
            'hangarID': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'})
        },
        'corp.wallet': {
            'Meta': {'ordering': "['walletID']", 'object_name': 'Wallet'},
            'walletID': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'})
        },
        'eve.blueprinttype': {
            'Meta': {'ordering': "['blueprintTypeID']", 'object_name': 'BlueprintType'},
            'blueprintTypeID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'data_interface': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'blueprint_datainterfaces'", 'null': 'True', 'db_column': "'dataInterfaceID'", 'to': "orm['eve.Type']"}),
            'materialModifier': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maxProductionLimit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_blueprint': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_blueprints'", 'null': 'True', 'db_column': "'parentBlueprintTypeID'", 'to': "orm['eve.BlueprintType']"}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['eve.Type']", 'unique': 'True', 'null': 'True', 'db_column': "'productTypeID'", 'blank': 'True'}),
            'productionTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'productivityModifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'researchCopyTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'researchMaterialTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'researchProductivityTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'researchTechTime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'techLevel': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wasteFactor': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve.category': {
            'Meta': {'ordering': "['categoryID']", 'object_name': 'Category'},
            'categoryID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'categoryName': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'iconID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        'eve.group': {
            'Meta': {'ordering': "['groupID']", 'object_name': 'Group'},
            'allowManufacture': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'allowRecycler': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'anchorable': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'anchored': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'db_column': "'categoryID'", 'to': "orm['eve.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fittableNonSingleton': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'groupID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'groupName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'iconID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'useBasePrice': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve.marketgroup': {
            'Meta': {'ordering': "['marketGroupID']", 'object_name': 'MarketGroup'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hasTypes': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'iconID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'marketGroupID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'marketGroupName': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'parent_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_groups'", 'null': 'True', 'db_column': "'parentGroupID'", 'to': "orm['eve.MarketGroup']"})
        },
        'eve.type': {
            'Meta': {'ordering': "['typeID']", 'object_name': 'Type'},
            'basePrice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'blueprint': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['eve.BlueprintType']", 'unique': 'True', 'null': 'True', 'db_column': "'blueprintTypeID'", 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'types'", 'db_column': "'categoryID'", 'to': "orm['eve.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'types'", 'db_column': "'groupID'", 'to': "orm['eve.Group']"}),
            'market_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items'", 'null': 'True', 'db_column': "'marketGroupID'", 'to': "orm['eve.MarketGroup']"}),
            'metaGroupID': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'portionSize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'raceID': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'techLevel': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'typeID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'typeName': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'hr.member': {
            'DoB': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['name']", 'object_name': 'Member'},
            'accessLvl': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'ancestry': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'baseID': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'bloodLine': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'characterID': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'charisma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charismaBonusName': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'charismaBonusValue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cloneName': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'cloneSkillPoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': "orm['corp.Corporation']"}),
            'corpDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intelligenceBonusName': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'intelligenceBonusValue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lastLogin': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastLogoff': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'???'", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'locationID': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'memory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'memoryBonusName': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'memoryBonusValue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'characters'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'perceptionBonusName': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'perceptionBonusValue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ship': ('django.db.models.fields.CharField', [], {'default': "'???'", 'max_length': '128'}),
            'willpower': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpowerBonusName': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'willpowerBonusValue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'hr.memberdiff': {
            'Meta': {'ordering': "['date']", 'object_name': 'MemberDiff'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('ecm.lib.bigintpatch.BigAutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'diffs'", 'to': "orm['hr.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'})
        },
        'hr.membersession': {
            'Meta': {'object_name': 'MemberSession'},
            'character_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'id': ('ecm.lib.bigintpatch.BigAutoField', [], {'primary_key': 'True'}),
            'session_begin': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'session_end': ('django.db.models.fields.DateTimeField', [], {}),
            'session_seconds': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        'hr.role': {
            'Meta': {'ordering': "['id']", 'object_name': 'Role'},
            'accessLvl': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'dispName': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'hangar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corp.Hangar']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'roles'", 'symmetrical': 'False', 'through': "orm['hr.RoleMembership']", 'to': "orm['hr.Member']"}),
            'roleID': ('django.db.models.fields.BigIntegerField', [], {}),
            'roleName': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'roleType': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': "orm['hr.RoleType']"}),
            'wallet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corp.Wallet']", 'null': 'True', 'blank': 'True'})
        },
        'hr.rolememberdiff': {
            'Meta': {'ordering': "['date']", 'object_name': 'RoleMemberDiff'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('ecm.lib.bigintpatch.BigAutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Member']"}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Role']"})
        },
        'hr.rolemembership': {
            'Meta': {'ordering': "['member']", 'object_name': 'RoleMembership'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Member']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Role']"})
        },
        'hr.roletype': {
            'Meta': {'ordering': "['dispName']", 'object_name': 'RoleType'},
            'dispName': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'typeName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'hr.skill': {
            'Meta': {'object_name': 'Skill'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['hr.Member']"}),
            'eve_type': ('ecm.lib.softfk.SoftForeignKey', [], {'to': "orm['eve.Type']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skillpoints': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'hr.title': {
            'Meta': {'ordering': "['titleID']", 'object_name': 'Title'},
            'accessLvl': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'titles'", 'to': "orm['corp.Corporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'titles'", 'symmetrical': 'False', 'through': "orm['hr.TitleMembership']", 'to': "orm['hr.Member']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'titles'", 'symmetrical': 'False', 'through': "orm['hr.TitleComposition']", 'to': "orm['hr.Role']"}),
            'tiedToBase': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'titleID': ('django.db.models.fields.BigIntegerField', [], {}),
            'titleName': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'hr.titlecompodiff': {
            'Meta': {'ordering': "['date']", 'object_name': 'TitleCompoDiff'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('ecm.lib.bigintpatch.BigAutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Role']"}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Title']"})
        },
        'hr.titlecomposition': {
            'Meta': {'ordering': "['title']", 'object_name': 'TitleComposition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Role']"}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Title']"})
        },
        'hr.titlememberdiff': {
            'Meta': {'ordering': "['date']", 'object_name': 'TitleMemberDiff'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('ecm.lib.bigintpatch.BigAutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Member']"}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Title']"})
        },
        'hr.titlemembership': {
            'Meta': {'ordering': "['member']", 'object_name': 'TitleMembership'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Member']"}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hr.Title']"})
        }
    }

    complete_apps = ['hr']