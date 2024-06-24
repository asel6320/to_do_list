from django.db import models

# Create your models here.
class ToDoList(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name="Description")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Status", default='new')
    deadline = models.DateField(auto_now=False, verbose_name="Deadline")

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status} - {self.deadline}"

    class Meta:
        db_table = 'toDoList'
        verbose_name = 'ToDoTask'
        verbose_name_plural = "ToDoList"
