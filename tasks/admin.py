from django.contrib import admin
from .models import Task, Comment, TaskHistory


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['created_at', 'updated_at']


class TaskHistoryInline(admin.TabularInline):
    model = TaskHistory
    extra = 0
    readonly_fields = ['timestamp']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'assigned_to', 'status', 'priority', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'created_at', 'due_date']
    search_fields = ['title', 'description', 'project__name', 'assigned_to__username']
    date_hierarchy = 'created_at'
    inlines = [CommentInline, TaskHistoryInline]
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'project')
        }),
        ('Assignment', {
            'fields': ('assigned_to', 'created_by')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority')
        }),
        ('Time Management', {
            'fields': ('due_date', 'estimated_hours', 'actual_hours', 'completed_at')
        }),
        ('Additional', {
            'fields': ('tags', 'attachments')
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'task__title', 'author__username']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(TaskHistory)
class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'field_changed', 'timestamp']
    list_filter = ['field_changed', 'timestamp']
    search_fields = ['task__title', 'user__username']
    readonly_fields = ['timestamp']
