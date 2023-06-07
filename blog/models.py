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


class Comments(models.Model):
    """"Комментарии"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=30)
    text_comment = models.TextField('Текст коммента', max_length=500)
    post = models.ForeignKey(Pin, verbose_name='Пост', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Коментарии'
