from django import forms
from django.forms import widgets

from webapp.models import ToDoList

status_choices = [('new', 'New'), ('in_progress', 'In progress'),  ('done', 'Done')]

class TaskForm(forms.Form):
    description = forms.CharField(max_length=50, required=True, label="description")
    status = forms.ChoiceField(
        choices=status_choices,
        required=True,
        label="status",
        widget=forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 200px;'})
    )
    full_description = forms.CharField(
        max_length=3000,
        required=True,
        label="full description",
        widget=widgets.Textarea(attrs={"cols": 20, "rows": 5, "placeholder": "full description"}),
    )
    deadline = forms.DateField(
        label="deadline",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

class TaskDeleteForm(forms.Form):
    tasks = forms.ModelMultipleChoiceField(
        queryset=ToDoList.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select tasks to delete"
    )



