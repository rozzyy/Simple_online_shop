# Generated by Django 3.0.6 on 2020-05-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200513_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
