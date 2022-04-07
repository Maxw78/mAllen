# Generated by Django 3.2.11 on 2022-04-07 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebShopApp', '0007_alter_profile_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_photo',
            field=models.ImageField(default='default.jpg', upload_to='product_photo/'),
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='WebShopApp.review'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='profile',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='WebShopApp.profile'),
            preserve_default=False,
        ),
    ]