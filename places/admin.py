from django.contrib import admin
from .models import *
from ContentManagement.models import Images
from django.contrib.contenttypes.admin import GenericTabularInline,GenericStackedInline




class imageinline(GenericTabularInline):
    model = Images

class imageinlines(GenericStackedInline):
    model = Images
    

@admin.register(State)
class AdminArticle(admin.ModelAdmin):
    search_fields = ["title"]
    # list_filter = ["title"]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(Country)
class AdminContactUs(admin.ModelAdmin):
    search_fields = ["title"]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

@admin.register(District)
class AdminContentSection(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["state",'state__country']

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    

@admin.register(Place)
class AdminImages(admin.ModelAdmin):
    search_fields = ['placename']
    list_filter = ["district",'district__state','district__state__country']
    inlines = [imageinline]


    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]