# Generated by Django 5.1.4 on 2025-01-28 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='send_location',
            field=models.CharField(default=9, max_length=150),
            preserve_default=False,
        ),
    ]
