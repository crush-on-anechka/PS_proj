# Generated by Django 4.0.5 on 2022-06-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0010_alter_owner_sobes_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='sobes_status',
            field=models.CharField(blank=True, choices=[('OK', 'Пройден'), ('DENY', 'Отказ'), ('Not_auditioned', 'Не собеседовался')], default='Not_auditioned', max_length=200, null=True, verbose_name='Статус собеседования'),
        ),
    ]
