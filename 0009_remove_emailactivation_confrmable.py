# Generated by Django 3.0.4 on 2020-07-03 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_emailactivation_confrmable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailactivation',
            name='confrmable',
        ),
    ]