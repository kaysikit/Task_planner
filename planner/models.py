from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name="Статус")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ['id', ]


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Задача")
    task = models.TextField(max_length=1000, verbose_name="Описание задачи")
    start_date = models.DateField(auto_now_add=True, verbose_name="Начало задачи")
    end_date = models.DateField(verbose_name="Конец задачи")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, verbose_name="Статус задачи")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ['end_date', 'title', ]
