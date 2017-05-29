# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from .models import Loja, TipoLoja

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


admin.site.register(Loja, LojaAdmin)
admin.site.register(TipoLoja)