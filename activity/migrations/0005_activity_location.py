# Generated by Django 3.2.25 on 2024-05-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_activity_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='location',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
