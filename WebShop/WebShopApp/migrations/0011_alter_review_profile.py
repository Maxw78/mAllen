# Generated by Django 3.2.11 on 2022-04-07 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebShopApp', '0010_alter_product_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WebShopApp.profile'),
        ),
    ]