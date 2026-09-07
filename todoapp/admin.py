from django.contrib import admin

from .models import AllTask, Status, TimeCategory


@admin.register(AllTask)
class AllTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'deadline', 'time_category', 'status', 'created_time')
    list_display_links = ('name', 'time_category', 'status')
    ordering = ('deadline', 'time_category')
    list_per_page = 15
    list_editable = ('deadline',)
    fields = ('name', 'time_category', 'deadline', 'description')
    list_filter = ('time_category__name', 'status__name', 'user')
    

@admin.register(TimeCategory)
class TimeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    fields = ('name',)
    ordering = ('id',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    fields = ('name',)
    ordering = ('id',)