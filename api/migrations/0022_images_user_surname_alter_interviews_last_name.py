# Generated by Django 4.2.1 on 2023-06-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_merge_0019_delete_newsimage_0020_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Фамилия'),
        ),
    ]