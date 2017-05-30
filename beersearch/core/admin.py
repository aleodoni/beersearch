# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from .models import Loja, TipoLoja, FabricaMalte, Malte, Lupulo, Fermento, FabricaFermento

class TipoLojaInline(admin.TabularInline):
	model = TipoLoja.lojas.through
	extra = 2
	verbose_name_plural = 'Tipos de Lojas'

class FermentoInline(admin.TabularInline):
	model = Fermento
	extra = 2	

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

class FabricaFermentoAdmin(admin.ModelAdmin):
	model = FabricaFermento
	inlines = [FermentoInline]

class FermentoAdmin(admin.ModelAdmin):
	model = Fermento
	list_filter = ['fabrica__nome', ]
	ordering = ('fabrica__nome', 'nome', )
	search_fields = ('nome', )	


admin.site.register(Loja, LojaAdmin)
admin.site.register(TipoLoja)
admin.site.register(FabricaMalte)
admin.site.register(Malte, MalteAdmin)
admin.site.register(Lupulo)
admin.site.register(Fermento, FermentoAdmin)
admin.site.register(FabricaFermento, FabricaFermentoAdmin)

