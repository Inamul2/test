# Generated by Django 4.1.3 on 2022-11-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='cgpa',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]