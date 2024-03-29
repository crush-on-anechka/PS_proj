# Generated by Django 4.0.5 on 2022-06-23 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_alter_dog_options_curator_add_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curator',
            options={'ordering': ['name'], 'verbose_name': 'Куратор', 'verbose_name_plural': 'Кураторы'},
        ),
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ['name'], 'verbose_name': 'Собака', 'verbose_name_plural': 'Собаки'},
        ),
        migrations.AlterField(
            model_name='curator',
            name='pound',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Приют'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО хозяина')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('passport_no', models.CharField(blank=True, max_length=10, null=True, verbose_name='Серия и номер паспорта')),
                ('passport_issued', models.CharField(blank=True, max_length=200, null=True, verbose_name='Кем выдан')),
                ('passport_code', models.CharField(blank=True, max_length=7, null=True, verbose_name='Код подразделения')),
                ('passport_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('address_reg', models.CharField(blank=True, max_length=500, null=True, verbose_name='Адрес регистрации')),
                ('address_fact', models.CharField(blank=True, max_length=500, null=True, verbose_name='Адрес проживания')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('tel', models.CharField(blank=True, max_length=10, null=True, verbose_name='Телефон без префикса (10 цифр)')),
                ('dog', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dogs.dog', verbose_name='Собака')),
            ],
            options={
                'verbose_name': 'Хозяин',
                'verbose_name_plural': 'Хозяева',
                'ordering': ['name'],
            },
        ),
    ]
