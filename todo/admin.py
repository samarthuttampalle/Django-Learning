from .models import Task
from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed',  'upadetd_at')
    search_fields = ('task',)
admin.site.register(Task, TaskAdmin)
