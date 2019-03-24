from django.contrib import admin
from django import forms
from timesheet.models import Customer, Project, Entry


class ProjectInline(admin.TabularInline):
    model = Project

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('date','user', 'customer','project','duration','description')
    list_filter = ('customer', 'user')
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)