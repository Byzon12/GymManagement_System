# Generated by Django 5.1.4 on 2025-04-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='UserName',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='password',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
