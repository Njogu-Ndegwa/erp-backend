# Generated by Django 3.2.9 on 2021-11-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
