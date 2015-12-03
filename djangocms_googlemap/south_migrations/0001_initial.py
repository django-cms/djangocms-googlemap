# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, connection


class Migration(SchemaMigration):

    def forwards(self, orm):
        table_names = connection.introspection.table_names()
        if 'cmsplugin_googlemap' in table_names or 'googlemap_googlemap' in table_names:
            # Rename tables
            if 'cmsplugin_googlemap' in table_names:
                db.rename_table('cmsplugin_googlemap', 'djangocms_googlemap_googlemap')
            elif 'googlemap_googlemap' in table_names:
                db.rename_table('googlemap_googlemap', 'djangocms_googlemap_googlemap')

            # South migrations are run twice, first as a dry run and then for real
            # Wait until the table is renamed for real before doing further work
            if not db.dry_run:
                # Check for missing fields from previous migrations
                # (0013_auto__add_field_googlemap_info_window__add_field_googlemap_scrollwheel.py)

                # Get existing columns
                description = connection.introspection.get_table_description(connection.cursor(), 'djangocms_googlemap_googlemap')
                columns = [c[0] for c in description]

                # Add missing columns
                if not 'info_window' in columns:
                    # Adding field 'GoogleMap.info_window'
                    db.add_column(u'djangocms_googlemap_googlemap', 'info_window',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'scrollwheel' in columns:
                    # Adding field 'GoogleMap.scrollwheel'
                    db.add_column(u'djangocms_googlemap_googlemap', 'scrollwheel',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'double_click_zoom' in columns:
                    # Adding field 'GoogleMap.double_click_zoom'
                    db.add_column(u'djangocms_googlemap_googlemap', 'double_click_zoom',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'draggable' in columns:
                    # Adding field 'GoogleMap.draggable'
                    db.add_column(u'djangocms_googlemap_googlemap', 'draggable',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'keyboard_shortcuts' in columns:
                    # Adding field 'GoogleMap.keyboard_shortcuts'
                    db.add_column(u'djangocms_googlemap_googlemap', 'keyboard_shortcuts',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'pan_control' in columns:
                    # Adding field 'GoogleMap.pan_control'
                    db.add_column(u'djangocms_googlemap_googlemap', 'pan_control',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'zoom_control' in columns:
                    # Adding field 'GoogleMap.zoom_control'
                    db.add_column(u'djangocms_googlemap_googlemap', 'zoom_control',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

                if not 'street_view_control' in columns:
                    # Adding field 'GoogleMap.street_view_control'
                    db.add_column(u'djangocms_googlemap_googlemap', 'street_view_control',
                                  self.gf('django.db.models.fields.BooleanField')(default=True),
                                  keep_default=False)

        else:
            # Adding model 'GoogleMap'
            db.create_table(u'djangocms_googlemap_googlemap', (
                (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
                ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
                ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
                ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=30)),
                ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
                ('content', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
                ('zoom', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=13)),
                ('lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('route_planer_title', self.gf('django.db.models.fields.CharField')(default=u'Calculate your fastest way to here', max_length=150, null=True, blank=True)),
                ('route_planer', self.gf('django.db.models.fields.BooleanField')(default=False)),
                ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=6)),
                ('height', self.gf('django.db.models.fields.CharField')(default='400px', max_length=6)),
                ('info_window', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('scrollwheel', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('double_click_zoom', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('draggable', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('keyboard_shortcuts', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('pan_control', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('zoom_control', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('street_view_control', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ))
            db.send_create_signal(u'djangocms_googlemap', ['GoogleMap'])

    def backwards(self, orm):
        # Deleting model 'GoogleMap'
        db.delete_table(u'djangocms_googlemap_googlemap')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'djangocms_googlemap.googlemap': {
            'Meta': {'object_name': 'GoogleMap', '_ormbases': ['cms.CMSPlugin']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'double_click_zoom': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'draggable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'info_window': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keyboard_shortcuts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'pan_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'route_planer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'route_planer_title': ('django.db.models.fields.CharField', [], {'default': "u'Calculate your fastest way to here'", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'scrollwheel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'street_view_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'zoom': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '13'}),
            'zoom_control': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['djangocms_googlemap']