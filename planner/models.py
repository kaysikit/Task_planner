from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title



