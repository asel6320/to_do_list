from django import forms
from django.forms import widgets

from webapp.models import ToDoList, Status, Type, ToDoListType



class TaskForm(forms.Form):
    description = forms.CharField(max_length=50, required=True, label="description")
    full_description = forms.CharField(
        max_length=3000,
        required=True,
        label="full description",
        widget=widgets.Textarea(attrs={"cols": 20, "rows": 5, "placeholder": "full description"}),
    )






