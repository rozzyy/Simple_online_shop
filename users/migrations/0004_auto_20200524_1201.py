# Generated by Django 3.0.6 on 2020-05-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200524_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.ImageField(default='user_default.png', upload_to='images/users/'),
        ),
    ]