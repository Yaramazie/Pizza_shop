from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'get_photo', 'available')
    list_display_links = ('title', 'content', 'get_photo')
    search_fields = ('title', 'price')
    list_editable = ('available', 'price')
    readonly_fields = ('get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Miniature'


class PizzaSliceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'available')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'price')
    list_editable = ('available', 'price')
    save_on_top = True


class PizzaRollAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'available')
    list_display_links = ('title', 'content', 'price',)
    search_fields = ('title', 'price')
    list_editable = ('available',)
    save_on_top = True


class TopingAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'available')
    list_display_links = ('title', 'content', 'price',)
    search_fields = ('title', 'price')
    list_editable = ('available',)
    save_on_top = True


class BoxAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'available')
    list_display_links = ('title', 'content', 'price',)
    search_fields = ('title', 'price')
    list_editable = ('available',)
    save_on_top = True


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(PizzaSlice, PizzaSliceAdmin)
admin.site.register(PizzaRoll, PizzaRollAdmin)
admin.site.register(Toping, TopingAdmin)
admin.site.register(Box, BoxAdmin)
