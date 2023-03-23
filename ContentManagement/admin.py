from django.contrib import admin
from .models import Article,Section,ContactUs

# Register your models here.

admin.site.register(Section)



@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    search_fields = ["art_title"]
    list_filter = ["section"]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(ContactUs)
class AdminContactUs(admin.ModelAdmin):
    search_fields = ["email"]

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]