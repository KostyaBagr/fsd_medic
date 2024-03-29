# Generated by Django 4.2.1 on 2023-06-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_user_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('email', models.CharField(max_length=100, null=True, unique=True, verbose_name='Электронный адрес')),
            ],
        ),
        migrations.CreateModel(
            name='NumberCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('number', models.CharField(max_length=30, null=True, unique=True, verbose_name='Номер')),
            ],
        ),
        migrations.DeleteModel(
            name='Country_Codes',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='number_code',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='number_length',
        ),
        migrations.DeleteModel(
            name='Email_Codes',
        ),
    ]
