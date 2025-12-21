from django.contrib import admin
from .models import Project, ProjectUpdate


class ProjectUpdateInline(admin.TabularInline):
    model = ProjectUpdate
    extra = 0
    readonly_fields = ['created_at']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'status', 'priority', 'start_date', 'created_at']
    list_filter = ['status', 'priority', 'created_at']
    search_fields = ['name', 'description', 'owner__username']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['members']
    date_hierarchy = 'created_at'
    inlines = [ProjectUpdateInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'owner')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority')
        }),
        ('Dates & Budget', {
            'fields': ('start_date', 'end_date', 'budget')
        }),
        ('Team', {
            'fields': ('members',)
        }),
    )


@admin.register(ProjectUpdate)
class ProjectUpdateAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content', 'project__name']
    readonly_fields = ['created_at']
