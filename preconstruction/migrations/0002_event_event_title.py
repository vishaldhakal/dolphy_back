# Generated by Django 3.1.6 on 2023-09-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preconstruction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_title',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
