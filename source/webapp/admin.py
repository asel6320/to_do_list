from django.contrib import admin

from webapp.models import ToDoList

# Register your models here.
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'deadline', 'full_description']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['status', 'description']
    fields = ['description', 'status', 'deadline', 'full_description']
    readonly_fields = ['deadline']

admin.site.register(ToDoList, ToDoListAdmin)