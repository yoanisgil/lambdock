from django.contrib import admin
from django.contrib.admin import site

from .models import Stack, Function, FunctionVersion


class StackAdmin(admin.ModelAdmin):
    model = Stack


class FunctionAdmin(admin.ModelAdmin):
    model = Function


class FunctionVersionAdmin(admin.ModelAdmin):
    model = FunctionVersion


site.register(Stack, StackAdmin)
site.register(Function, FunctionAdmin)
site.register(FunctionVersion, FunctionVersionAdmin)
