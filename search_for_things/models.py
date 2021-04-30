from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class Thing(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование словаря',)

    def __str__(self):
        return self.title


class StolenItem(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО',)
    date_of_birth = models.DateField(verbose_name='Дата рождения',)
    residential_address = models.TextField(verbose_name='Адрес проживания',)
    phone_number = models.CharField(max_length=15, verbose_name='Контактный телефон', blank=True, null=True)
    item = models.ForeignKey(Thing,
                             related_name='item_stolen',
                             on_delete=models.PROTECT,
                             verbose_name='Вещь',
                             )
    vin = models.CharField(max_length=255, verbose_name='Номер',)
    description = models.TextField(verbose_name='Описание', blank=True, null=True,)
    create_ad = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True,)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    check_find = models.BooleanField(verbose_name='Найден', default=None,)

    def __str__(self):
        return self.name


class PictureStolen(models.Model):
    name = models.ForeignKey(StolenItem,
                             verbose_name='Связь с лицом',
                             related_name='stolen',
                             on_delete=models.PROTECT,
                             )
    image = models.TextField(verbose_name='Картинка',)
    file_id_api = models.TextField( verbose_name='file_id from API Telegram',)

    def __str__(self):
        return str(self.pk)


class PersonWithThing(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО',)
    date_of_birth = models.DateField(verbose_name='Дата рождения',)
    residential_address = models.TextField(verbose_name='Адрес проживания',)
    phone_number = models.CharField(max_length=15, verbose_name='Контактный телефон', blank=True, null=True)
    item = models.ForeignKey(Thing,
                             related_name='item_person',
                             on_delete=models.PROTECT,
                             verbose_name='Вещь',
                             )
    vin = models.CharField(max_length=255, verbose_name='Номер', )
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    create_ad = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True,)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class PicturePerson(models.Model):
    name = models.ForeignKey(PersonWithThing,
                             related_name='person',
                             on_delete=models.PROTECT,
                             verbose_name='Связь с лицом'
                             )
    image = models.TextField(verbose_name='Картинка',)
    file_id_api = models.TextField( verbose_name='file_id from API Telegram',)

    def __str__(self):
        return str(self.name)
