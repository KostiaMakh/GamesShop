from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

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
    list_display = (
        'status',
        'is_default'
    )
    list_editable = ('is_default',)
    search_fields = (
        'status',
        'is_default'
    )
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
    search_fields = ('title',)
    list_filter = (
        'is_published',
        'status',
    )
    list_display = ('id',
                    'title',
                    'price',
                    'old_price',
                    'get_poster',
                    'is_published',
                    'status',
                    )
    save_on_top = True
    exclude = (
        'slug',
        'buys',
        'owner',
        'created_at',
        'updated_at',
    )

    def get_poster(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" height="80px"')

    get_poster.short_description = 'Poster'


admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Promo, PromoAdmin)
