# Generated by Django 3.1.2 on 2021-02-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='lead_source',
        ),
        migrations.AlterField(
            model_name='lead',
            name='state',
            field=models.CharField(choices=[('News Paper', 'News Paper'), ('Magazine', 'Magazine'), ('Advertising', 'Advertising'), ('Google', 'Google'), ('Gmail', 'Gmail')], max_length=50),
        ),
    ]
