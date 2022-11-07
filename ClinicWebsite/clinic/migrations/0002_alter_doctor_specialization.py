# Generated by Django 4.1.3 on 2022-11-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('General Doctor', 'General Doctor'), ('Emergency Doctor', 'Emergency Doctor'), ('Orthopedics Doctor', 'Orthopedics Doctor')], max_length=256),
        ),
    ]