# Generated by Django 5.1.4 on 2025-02-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_rename_suplan_subfeature_subplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='max_member',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
