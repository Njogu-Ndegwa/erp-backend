# Generated by Django 3.2.9 on 2021-11-04 02:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maincategories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100, null=True)),
                ('created_at', models.CharField(max_length=100)),
                ('updated_at', models.CharField(max_length=100, null=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maincategories.maincategory')),
            ],
        ),
    ]
