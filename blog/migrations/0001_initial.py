# Generated by Django 5.1.7 on 2025-03-30 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='blogs')),
                ('comment', models.TextField()),
                ('like', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2025, 3, 30, 0, 35, 12, 733117, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2025, 3, 30, 0, 35, 12, 733264, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
