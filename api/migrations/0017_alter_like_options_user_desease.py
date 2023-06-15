# Generated by Django 4.2.1 on 2023-06-15 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_groups_number_of_people'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name_plural': 'Лайки'},
        ),
        migrations.AddField(
            model_name='user',
            name='desease',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.desease', verbose_name='Заболевание'),
        ),
    ]
