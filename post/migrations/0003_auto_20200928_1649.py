# Generated by Django 3.1.1 on 2020-09-28 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200928_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='lats_updated',
            new_name='last_updated',
        ),
    ]
