# Generated by Django 4.2.7 on 2023-11-17 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_userprofile_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='reorder_level',
            new_name='reorder_quantity',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='role',
            new_name='role_role',
        ),
    ]
