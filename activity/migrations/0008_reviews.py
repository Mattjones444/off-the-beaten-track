# Generated by Django 3.2.25 on 2024-06-09 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_rename_price_per_person_activity_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(blank=True, max_length=150, null=True)),
                ('review_rating', models.IntegerField()),
                ('review_description', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('activity_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.activity')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
