from django.db import migrations, models


def reset_null_values(apps, schema_editor):
    GoogleMap = apps.get_model('djangocms_googlemap', 'GoogleMap')
    plugins = GoogleMap.objects.all()
    plugins.filter(title__isnull=True).update(title='')


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0006_remove_fields'),
    ]

    operations = [
        migrations.RunPython(reset_null_values),
    ]
