# Generated by Django 3.2.7 on 2021-11-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='valid_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='valid_to',
            field=models.DateField(),
        ),
    ]
