# Generated by Django 4.2.1 on 2023-06-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_interviews_is_center_interview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centers',
            name='number',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='number',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Номер'),
        ),
    ]