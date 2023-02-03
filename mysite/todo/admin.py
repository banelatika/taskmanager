from django.contrib import admin
from todo.models import profile, TaskUser

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'is_active', 'is_admin', 'gruop')


@admin.register(TaskUser)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'id','checkbox', 'taskdetails', 'assignee', 'assignor')


