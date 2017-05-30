# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from .models import Loja, TipoLoja, FabricaMalte, Malte, Lupulo

class TipoLojaInline(admin.TabularInline):
	model = TipoLoja.lojas.through
	extra = 2
	verbose_name_plural = 'Tipos de Lojas'

class LojaAdmin(admin.ModelAdmin):
	model = Loja
	list_filter = ['tipoloja__nome', ]
	ordering = ('nome',)
	search_fields = ('nome', )
	inlines = [TipoLojaInline]

class MalteAdmin(admin.ModelAdmin):
	model = Malte
	list_filter = ['fabrica__nome', ]
	ordering = ('fabrica__nome', 'nome', )
	search_fields = ('nome', )


admin.site.register(Loja, LojaAdmin)
admin.site.register(TipoLoja)
admin.site.register(FabricaMalte)
admin.site.register(Malte, MalteAdmin)
admin.site.register(Lupulo)