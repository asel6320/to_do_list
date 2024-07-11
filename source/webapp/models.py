from django.db import models

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="Status")

    def __str__(self):
        return self.name
    class Meta:
        db_table = "statuses"
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class Type(models.Model):
    name = models.CharField(max_length=31, verbose_name='Type', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "types"
        verbose_name = "Type"
        verbose_name_plural = "Types"

class ToDoList(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name="Description")
    full_description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Full Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    status = models.ForeignKey('webapp.Status', related_name='to_do_list', on_delete=models.RESTRICT, verbose_name="Status")
    types = models.ManyToManyField(
        "webapp.Type",
        related_name="to_do_list",
        verbose_name="Types",
        blank=True,
        through='webapp.ToDoListType',
        through_fields=("toDoList", "type"),
    )

    def __str__(self):
        return f"{self.pk}. {self.description} - {self.full_description}| - {self.created_at} - {self.updated_at}"

    class Meta:
        db_table = 'to_do_list'
        verbose_name = 'ToDoTask'
        verbose_name_plural = "ToDoList"

class ToDoListType(models.Model):
    toDoList = models.ForeignKey('webapp.ToDoList', related_name='types_tasks', on_delete=models.RESTRICT, )
    type = models.ForeignKey('webapp.Type', related_name='tasks_types', on_delete=models.RESTRICT, )

    def __str__(self):
        return f"Task: {self.toDoList.description} - Type: {self.type.name}"