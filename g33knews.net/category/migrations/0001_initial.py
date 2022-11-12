# Generated by Django 4.1.3 on 2022-11-12 18:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('categoryengname', models.CharField(max_length=500, verbose_name='English Name Of Categroy')),
                ('categorypersianname', models.CharField(max_length=500, verbose_name='Persian Name Of Categroy')),
                ('typeofcategory', models.IntegerField(choices=[(0, 'Main'), (1, 'Sub')], default=0, verbose_name='Type Of Category ')),
                ('active', models.BooleanField(default=True, verbose_name='Active ?')),
            ],
        ),
    ]
