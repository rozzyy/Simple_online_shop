# Generated by Django 3.0.6 on 2020-05-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200517_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.IntegerField(default=0),
        ),
    ]
