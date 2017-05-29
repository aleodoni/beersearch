# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#---------------------------------------------------------------------------------------------
# Model Loja
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class Loja(models.Model):
	class Meta:
		verbose_name_plural = 'Lojas'

	nome = models.CharField(max_length=300)
	site = models.URLField()
	email = models.EmailField()

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome

#---------------------------------------------------------------------------------------------
# Model TipoLoja
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class TipoLoja(models.Model):
	class Meta:
		verbose_name_plural = 'Tipos de Lojas'

	nome = models.CharField(max_length=300)
	lojas = models.ManyToManyField(Loja, blank=True)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome		

#---------------------------------------------------------------------------------------------
# Model FabricaMalte
#---------------------------------------------------------------------------------------------
@python_2_unicode_compatible
class FabricaMalte(models.Model):
	class Meta:
		verbose_name_plural = 'Fabricas de Maltes'

	nome = models.CharField(max_length=300)
	pais = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome				