# Generated by Django 4.2.7 on 2023-11-17 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_rename_created_at_item_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='role_role',
            new_name='user_role',
        ),
    ]
