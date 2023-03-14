from django.contrib import admin
from faqs.models import *


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'language']


admin.site.register(Language, LanguageAdmin)
admin.site.register(Faq, FaqAdmin)

