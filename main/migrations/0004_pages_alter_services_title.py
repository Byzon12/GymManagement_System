# Generated by Django 5.1.4 on 2025-01-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_services_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
