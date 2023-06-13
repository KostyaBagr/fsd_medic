# Generated by Django 4.2.1 on 2023-06-07 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Логин')),
                ('is_required', models.BooleanField(default=False, verbose_name='Статус подтверждения')),
                ('is_patient', models.BooleanField(default=False, verbose_name='Статус пациента')),
                ('is_doctor', models.BooleanField(default=False, verbose_name='Статус доктора')),
                ('is_center_admin', models.BooleanField(default=False, verbose_name='Статус администратора центра')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус персонала')),
                ('number', models.CharField(max_length=30, null=True, unique=True, verbose_name='Номер')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Электронный адрес')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Фамилия')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('group', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('is_required', models.BooleanField(default=False, verbose_name='Статус подтверждения')),
                ('number', models.PositiveBigIntegerField(null=True, unique=True, verbose_name='Номер')),
                ('email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='Электронный адрес')),
                ('employees_number', models.IntegerField(null=True, verbose_name='Число Сотрудников')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('address', models.CharField(max_length=100, null=True, unique=True, verbose_name='Адрес')),
                ('coordinate_latitude', models.FloatField(null=True, verbose_name='Широта')),
                ('coordinate_longitude', models.FloatField(null=True, verbose_name='Долгата')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата Изменения')),
            ],
            options={
                'verbose_name_plural': 'Центры',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название страны')),
                ('number_code', models.CharField(max_length=15, null=True, verbose_name='Телефонный код страны')),
            ],
            options={
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата интервью')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, null=True, verbose_name='Фамилия')),
                ('number', models.PositiveBigIntegerField(null=True, unique=True, verbose_name='Номер')),
                ('email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='Электронный адрес')),
                ('is_center_interview', models.BooleanField(default=False, verbose_name='Статус принодлежности к центру')),
                ('is_doctor_interview', models.BooleanField(default=False, verbose_name='Статус принодлежности к доктору')),
                ('is_required', models.BooleanField(default=False, verbose_name='Статус подтверждения')),
                ('application', models.CharField(max_length=30, null=True, verbose_name='Приложение')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name_plural': 'Интервью',
            },
        ),
        migrations.CreateModel(
            name='Url_Params',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=50)),
                ('interview', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.interviews')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Email_Codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]