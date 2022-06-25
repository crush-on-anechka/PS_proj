from django.contrib import admin
from .models import Dog, Curator, Owner, Adoption


class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'curator', 'add_date')
    list_editable = ('curator',)
    search_fields = ('name',)
    list_filter = ('add_date',)
    empty_value_display = '-пусто-'


class CuratorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'pound')
    search_fields = ('pound',)
    empty_value_display = '-пусто-'


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'add_date')
    search_fields = ('dog',)
    list_filter = ('add_date',)
    empty_value_display = '-пусто-'


class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'dog', 'add_date')
    search_fields = ('owner', 'dog',)
    list_filter = ('add_date',)
    empty_value_display = '-пусто-'


admin.site.register(Dog, DogAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Adoption, AdoptionAdmin)
