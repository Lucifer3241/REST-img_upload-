# Generated by Django 4.1.6 on 2023-04-16 02:42

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_airport_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=api.models.upload_to)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='api.airport')),
            ],
        ),
    ]
