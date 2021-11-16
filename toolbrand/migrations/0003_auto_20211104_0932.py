# Generated by Django 3.2.9 on 2021-11-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbrand', '0002_itembrand_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itembrand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='itembrand',
            name='status',
            field=models.CharField(default='PENDING', max_length=100),
        ),
    ]
