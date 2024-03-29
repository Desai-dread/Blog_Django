# Generated by Django 4.2.1 on 2023-06-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=52, verbose_name='Заголовочек')),
                ('subTitle', models.TextField(verbose_name='Подзаголовок')),
                ('author', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('date', models.DateField(verbose_name='Дата поста')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
