from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
    Genre,
    Game,
    Device,
    Status,
    Company,
    Language,
    Promo,
    ScreenShot,
)


class ContentField(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    form = ContentField
    save_on_top = True
    exclude = ('slug',)


class StatusAdmin(admin.ModelAdmin):
    model = Status
    save_on_top = True
    list_display = ('status', 'is_default')
    list_editable = ('is_default',)
    search_fields = ('status', 'is_default')
    exclude = ('slug',)


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    save_on_top = True
    exclude = ('slug',)


class LanguageAdmin(admin.ModelAdmin):
    model = Language
    save_on_top = True
    exclude = ('slug',)


class PromoAdmin(admin.ModelAdmin):
    model = Promo
    save_on_top = True
    exclude = ('slug',)


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    form = ContentField
    save_on_top = True
    exclude = ('slug',)


class ScreenShortsInline(admin.TabularInline):
    fk_name = 'game'
    model = ScreenShot


class GameAdmin(admin.ModelAdmin):
    model = Company
    form = ContentField
    inlines = [ScreenShortsInline, ]
    save_on_top = True
    exclude = (
        'slug',
        'buys',
        'owner',
        'created_at',
        'updated_at',
    )

    # def get_photo(self, obj):
    #     if obj.photo:
    #         return mark_safe(f'<img src="{obj.photo.url}" width="75px">')
    #
    # get_photo.short_description = 'Фото'


admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Promo, PromoAdmin)
