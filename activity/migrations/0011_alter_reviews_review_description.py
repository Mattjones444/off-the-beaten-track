# Generated by Django 3.2.25 on 2024-06-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_alter_reviews_review_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_description',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
