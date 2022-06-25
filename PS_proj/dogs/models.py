from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CHOICES = [
            ('OK', 'Пройдено'),
            ('DENY', 'Отказ'),
            ('Not_auditioned', 'Не собеседовался')
        ]


class Curator(models.Model):
    name = models.CharField('ФИО куратора', max_length=200)
    tel = models.CharField(
        'Телефон без префикса (10 цифр)',
        max_length=10
    )
    pound = models.CharField(
        'Приют',
        max_length=200,
        blank=True,
        null=True
    )
    add_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )
    passport_no = models.CharField(
        'Серия и номер паспорта',
        max_length=10,
        blank=True,
        null=True
    )
    passport_issued = models.CharField(
        'Кем выдан',
        max_length=200,
        blank=True,
        null=True
    )
    passport_code = models.CharField(
        'Код подразделения',
        max_length=7,
        blank=True,
        null=True
    )
    passport_date = models.DateField(
        'Дата выдачи',
        blank=True,
        null=True
    )
    address_reg = models.CharField(
        'Адрес регистрации',
        max_length=500,
        blank=True,
        null=True
    )
    email = models.EmailField(
        'Email',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField('Кличка', max_length=200)
    curator = models.ForeignKey(
        Curator,
        on_delete=models.SET_NULL,
        null=True,
        max_length=200,
        related_name='curator',
        verbose_name="Куратор"
    )
    add_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField('ФИО хозяина', max_length=200)
    tel = models.CharField(
        'Телефон без префикса (10 цифр)',
        max_length=10
    )

    add_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )
    passport_no = models.CharField(
        'Серия и номер паспорта',
        max_length=10,
        blank=True,
        null=True
    )
    passport_issued = models.CharField(
        'Кем выдан',
        max_length=200,
        blank=True,
        null=True
    )
    passport_code = models.CharField(
        'Код подразделения',
        max_length=7,
        blank=True,
        null=True
    )
    passport_date = models.DateField(
        'Дата выдачи',
        blank=True,
        null=True
    )
    address_reg = models.CharField(
        'Адрес регистрации',
        max_length=500,
        blank=True,
        null=True
    )
    address_fact = models.CharField(
        'Адрес проживания',
        max_length=500,
        blank=True,
        null=True
    )
    email = models.EmailField(
        'Email',
        blank=True,
        null=True
    )
    discount_card = models.CharField(
        'Номер карты Коммондор',
        max_length=10,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-add_date']
        verbose_name = "Хозяин"
        verbose_name_plural = "Хозяева"

    def __str__(self):
        return self.name


class Adoption(models.Model):
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='dog_owner',
        verbose_name='Хозяин'
    )
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE,
        related_name='adopted_dog',
        verbose_name='Собака'
    )
    add_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )
    contract_signed = models.BooleanField(
        'Договор подписан',
        default=False,
        blank=True,
        null=True
    )
    sobes_status = models.CharField(
        'Статус собеседования',
        max_length=200,
        choices=CHOICES,
        default='Not_auditioned',
        blank=False,
        null=True
    )
    sobes_result = models.TextField(
        'Комментарий',
        max_length=1000,
        blank=True,
        null=True
    )
    had_pets = models.BooleanField(
        'Были ли домашние животные',
        blank=True,
        null=True
    )
    large_place = models.BooleanField(
        'Огромная квартира',
        blank=True,
        null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'dog'],
                name='unique_adoption'
            )
        ]
        ordering = ['-add_date']
        verbose_name = "Пристройство"
        verbose_name_plural = "Пристройства"

    def __str__(self):
        adoption = f'{self.owner} и {self.dog}'
        return adoption
