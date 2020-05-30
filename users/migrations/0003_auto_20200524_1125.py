# Generated by Django 3.0.6 on 2020-05-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(default='Lorem ipsum Dolor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/users/'),
        ),
    ]