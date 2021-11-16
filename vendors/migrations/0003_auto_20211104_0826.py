# Generated by Django 3.2.9 on 2021-11-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_vendor_is_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='first_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
