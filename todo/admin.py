from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'created', 'is_deleted')
    list_filter = ('is_deleted', )
    actions = ['restore_todo']

    def restore_todo(self, request, queryset):
        queryset.update(is_deleted=False)


admin.site.register(Todo, TodoAdmin)


