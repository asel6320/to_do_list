from django.contrib import admin
from django.forms import CheckboxSelectMultiple, ModelForm

from webapp.models import ToDoList, Status, Type, ToDoListType

class TagsInline(admin.TabularInline):
    model = ToDoList.types.through
# Register your models here.
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'full_description', 'created_at', 'updated_at']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['status', 'description']
    fields = ['description', 'full_description', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [
        TagsInline,
    ]


admin.site.register(ToDoList, ToDoListAdmin)

admin.site.register(Status)

admin.site.register(Type)

admin.site.register(ToDoListType)