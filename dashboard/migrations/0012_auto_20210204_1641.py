# Generated by Django 3.1.2 on 2021-02-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210204_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='follow_up_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='follow_up_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='inquiry_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='inquiry_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
