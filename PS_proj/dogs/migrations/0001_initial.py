# Generated by Django 4.0.5 on 2022-06-21 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО куратора')),
                ('pound', models.CharField(max_length=200, verbose_name='Приют')),
            ],
            options={
                'verbose_name': 'Куратор',
                'verbose_name_plural': 'Кураторы',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Кличка')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('curator', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dogs.curator', verbose_name='Куратор')),
            ],
            options={
                'verbose_name': 'Собака',
                'verbose_name_plural': 'Собаки',
            },
        ),
    ]
