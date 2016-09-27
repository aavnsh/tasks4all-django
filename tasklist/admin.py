from django.contrib import admin

from tasklist.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority')
    ordering = ('due_date', 'priority', 'title')
    search_fields = ('name',)

admin.site.register(Item, ItemAdmin)