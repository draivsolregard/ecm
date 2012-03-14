#@PydevCodeAnalysisIgnore
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CatalogEntry'
        db.create_table('industry_catalogentry', (
            ('typeID', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('typeName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fixed_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('production_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('public_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('industry', ['CatalogEntry'])

        # Adding model 'OwnedBlueprint'
        db.create_table('industry_ownedblueprint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typeID', self.gf('django.db.models.fields.IntegerField')()),
            ('me', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('pe', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('copy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('runs', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('catalog_entry', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='blueprints', null=True, to=orm['industry.CatalogEntry'])),
        ))
        db.send_create_signal('industry', ['OwnedBlueprint'])

        # Adding model 'SupplySource'
        db.create_table('industry_supplysource', (
            ('location_id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('industry', ['SupplySource'])

        # Adding model 'Supply'
        db.create_table('industry_supply', (
            ('typeID', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('auto_update', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('supply_source', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='prices', to=orm['industry.SupplySource'])),
        ))
        db.send_create_signal('industry', ['Supply'])

        # Adding model 'PriceHistory'
        db.create_table('industry_pricehistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supply', self.gf('django.db.models.fields.related.ForeignKey')(related_name='price_histories', to=orm['industry.Supply'])),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('industry', ['PriceHistory'])

        # Adding model 'InventionPolicy'
        db.create_table('industry_inventionpolicy', (
            ('item_group_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('item_group', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('invention_chance', self.gf('django.db.models.fields.FloatField')()),
            ('target_me', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('industry', ['InventionPolicy'])

        # Adding model 'Job'
        db.create_table('industry_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jobs', null=True, to=orm['industry.Order'])),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jobs', null=True, to=orm['industry.OrderRow'])),
            ('parent_job', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='childrenJobs', null=True, to=orm['industry.Job'])),
            ('state', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jobs', null=True, to=orm['auth.User'])),
            ('item_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('runs', self.gf('django.db.models.fields.FloatField')()),
            ('blueprint', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jobs', null=True, to=orm['industry.OwnedBlueprint'])),
            ('activity', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('industry', ['Job'])

        # Adding model 'Order'
        db.create_table('industry_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('originator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders_created', to=orm['auth.User'])),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='orders_manufactured', null=True, to=orm['auth.User'])),
            ('delivery_boy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='orders_delivered', null=True, to=orm['auth.User'])),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('delivery_location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('delivery_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('quote', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('industry', ['Order'])

        # Adding model 'OrderLog'
        db.create_table('industry_orderlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='logs', to=orm['industry.Order'])),
            ('state', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='logs', to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('industry', ['OrderLog'])

        # Adding model 'OrderRow'
        db.create_table('industry_orderrow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['industry.Order'])),
            ('catalog_entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='order_rows', to=orm['industry.CatalogEntry'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('industry', ['OrderRow'])


    def backwards(self, orm):
        
        # Deleting model 'CatalogEntry'
        db.delete_table('industry_catalogentry')

        # Deleting model 'OwnedBlueprint'
        db.delete_table('industry_ownedblueprint')

        # Deleting model 'SupplySource'
        db.delete_table('industry_supplysource')

        # Deleting model 'Supply'
        db.delete_table('industry_supply')

        # Deleting model 'PriceHistory'
        db.delete_table('industry_pricehistory')

        # Deleting model 'InventionPolicy'
        db.delete_table('industry_inventionpolicy')

        # Deleting model 'Job'
        db.delete_table('industry_job')

        # Deleting model 'Order'
        db.delete_table('industry_order')

        # Deleting model 'OrderLog'
        db.delete_table('industry_orderlog')

        # Deleting model 'OrderRow'
        db.delete_table('industry_orderrow')


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
        'industry.catalogentry': {
            'Meta': {'object_name': 'CatalogEntry'},
            'fixed_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'production_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'public_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'typeID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'typeName': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'industry.inventionpolicy': {
            'Meta': {'ordering': "['target_me', 'item_group_id']", 'object_name': 'InventionPolicy'},
            'invention_chance': ('django.db.models.fields.FloatField', [], {}),
            'item_group': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'item_group_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'target_me': ('django.db.models.fields.IntegerField', [], {})
        },
        'industry.job': {
            'Meta': {'ordering': "['order', 'id']", 'object_name': 'Job'},
            'activity': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'blueprint': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jobs'", 'null': 'True', 'to': "orm['industry.OwnedBlueprint']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jobs'", 'null': 'True', 'to': "orm['industry.Order']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jobs'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent_job': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'childrenJobs'", 'null': 'True', 'to': "orm['industry.Job']"}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jobs'", 'null': 'True', 'to': "orm['industry.OrderRow']"}),
            'runs': ('django.db.models.fields.FloatField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'industry.order': {
            'Meta': {'ordering': "['id']", 'object_name': 'Order'},
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'delivery_boy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'orders_delivered'", 'null': 'True', 'to': "orm['auth.User']"}),
            'delivery_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'delivery_location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'orders_manufactured'", 'null': 'True', 'to': "orm['auth.User']"}),
            'originator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders_created'", 'to': "orm['auth.User']"}),
            'quote': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'state': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'industry.orderlog': {
            'Meta': {'ordering': "['order', 'date']", 'object_name': 'OrderLog'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['industry.Order']"}),
            'state': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['auth.User']"})
        },
        'industry.orderrow': {
            'Meta': {'ordering': "['order']", 'object_name': 'OrderRow'},
            'catalog_entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order_rows'", 'to': "orm['industry.CatalogEntry']"}),
            'cost': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': "orm['industry.Order']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'industry.ownedblueprint': {
            'Meta': {'ordering': "['typeID', '-me']", 'object_name': 'OwnedBlueprint'},
            'catalog_entry': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'blueprints'", 'null': 'True', 'to': "orm['industry.CatalogEntry']"}),
            'copy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'me': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'pe': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'runs': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'typeID': ('django.db.models.fields.IntegerField', [], {})
        },
        'industry.pricehistory': {
            'Meta': {'ordering': "['supply', '-date']", 'object_name': 'PriceHistory'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'supply': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'price_histories'", 'to': "orm['industry.Supply']"})
        },
        'industry.supply': {
            'Meta': {'ordering': "['typeID']", 'object_name': 'Supply'},
            'auto_update': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'supply_source': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'prices'", 'to': "orm['industry.SupplySource']"}),
            'typeID': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'})
        },
        'industry.supplysource': {
            'Meta': {'ordering': "['name']", 'object_name': 'SupplySource'},
            'location_id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['industry']
