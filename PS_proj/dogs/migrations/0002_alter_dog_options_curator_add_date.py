# Generated by Django 4.0.5 on 2022-06-21 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ['-add_date'], 'verbose_name': 'Собака', 'verbose_name_plural': 'Собаки'},
        ),
        migrations.AddField(
            model_name='curator',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления'),
            preserve_default=False,
        ),
    ]