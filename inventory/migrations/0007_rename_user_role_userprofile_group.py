# Generated by Django 4.2.7 on 2023-11-24 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_rename_reorder_quantity_item_min_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_role',
            new_name='group',
        ),
    ]
