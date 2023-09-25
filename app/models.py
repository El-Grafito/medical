from django.db import models

class Client(models.Model):
    name = models.CharField('Имя',max_length=100)
    phone = models.CharField('Телефонный номер',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class Blog(models.Model):
    image = models.ImageField('Фото')
    title = models.CharField('Название',max_length=100)
    text = models.TextField('Текст')
    date = models.DateField('дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Sponsor(models.Model):
    name = models.CharField('Название',max_length=100)
    image = models.ImageField('Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'