# Generated by Django 3.1.2 on 2021-02-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_lead_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
