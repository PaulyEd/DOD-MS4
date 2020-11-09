from django.contrib import admin
from .models import Developer, Framework, Language, Spoken_Language

# Register your models here.


class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_framework',
        'get_language',
        'rate',
        'rating',
        'image',
    )

    def get_framework(self, obj):
        return ", ".join([p.friendly_name for p in obj.framework.all()])
        
    def get_language(self, obj):
        return ", ".join([p.friendly_name for p in obj.language.all()])

    ordering = ('name',)


class FrameworkAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Spoken_LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'nativeName',
    )

    ordering = ('name',)


admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Spoken_Language, Spoken_LanguageAdmin)
