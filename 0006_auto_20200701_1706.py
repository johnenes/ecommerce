# Generated by Django 3.0.4 on 2020-07-01 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200528_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='active',
            new_name='is_active',
        ),
    ]
