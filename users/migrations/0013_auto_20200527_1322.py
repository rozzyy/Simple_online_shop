# Generated by Django 3.0.6 on 2020-05-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200527_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.ImageField(default='/media/user_default.png', upload_to='images/'),
        ),
    ]
