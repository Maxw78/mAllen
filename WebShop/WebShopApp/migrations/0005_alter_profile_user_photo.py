# Generated by Django 3.2.11 on 2022-04-06 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebShopApp', '0004_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_photo',
            field=models.ImageField(default='default.jpg', upload_to='user_photo/'),
        ),
    ]
