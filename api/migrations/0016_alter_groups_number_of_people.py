# Generated by Django 4.2.1 on 2023-06-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_groups_number_of_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='number_of_people',
            field=models.IntegerField(default=0, verbose_name='Количество людей'),
        ),
    ]
