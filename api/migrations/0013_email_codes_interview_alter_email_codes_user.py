# Generated by Django 4.2.1 on 2023-06-09 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_codes',
            name='interview',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.interviews'),
        ),
        migrations.AlterField(
            model_name='email_codes',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]