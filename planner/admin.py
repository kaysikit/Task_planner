from django.contrib import admin

from .models import Task, Status


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status')
    list_display_links = ('title',)
    search_fields = ('title', 'end_date', 'status')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
