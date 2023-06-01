from django.db import models

class Pin(models.Model):
# Атрбуты  записи
    tittle = models.CharField('Заголовочек', max_length=52)
    subTitle = models.TextField('Текст')
    author = models.CharField('Имя автора', max_length=250)
    date = models.DateField('Дата поста')


    def __str__(self):
        return f'{self.tittle}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

