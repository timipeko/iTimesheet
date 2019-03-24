from django.contrib import admin
from django import forms
from timesheet.models import Customer, Project, Entry
from django.shortcuts import get_object_or_404


class ProjectInline(admin.TabularInline):
    model = Project

class EntryInline(admin.TabularInline):
    model = Entry

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [EntryInline]


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('date','user', 'customer','project','duration','description')
    list_filter = ('customer', 'project', 'user')
    exclude = ['user',]

    def get_queryset(self, request):
        qs = super(EntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)