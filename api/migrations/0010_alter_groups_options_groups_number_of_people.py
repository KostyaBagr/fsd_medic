# Generated by Django 4.2.1 on 2023-06-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_groups_user_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name_plural': 'Группы'},
        ),
        migrations.AddField(
            model_name='groups',
            name='number_of_people',
            field=models.IntegerField(null=True, verbose_name='Количество людей'),
        ),
    ]