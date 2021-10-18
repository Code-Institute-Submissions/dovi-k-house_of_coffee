# Generated by Django 3.2.7 on 2021-10-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_of_measure',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]