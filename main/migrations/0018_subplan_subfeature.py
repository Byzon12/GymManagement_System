# Generated by Django 5.1.4 on 2025-02-12 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_gallery_detail_galleryimage_alt_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('price', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Subfeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('subplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subplan')),
            ],
        ),
    ]
