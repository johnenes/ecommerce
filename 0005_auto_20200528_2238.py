# Generated by Django 3.0.5 on 2020-05-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200528_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_names',
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
