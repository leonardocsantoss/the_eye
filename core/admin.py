from django.contrib import admin
from core.models import Application, Session, Event


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'host')
    search_fields = ('name', 'host',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'timestamp')
    list_filter = ('category', 'timestamp',)
    search_fields = ('name', 'id', 'session__id',)
    raw_id_fields = ('session',)
    readonly_fields = ('created_at',)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', )
    raw_id_fields = ('application',)
    readonly_fields = ('created_at',)