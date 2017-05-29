# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from django.db import IntegrityError, DataError

from ..models import Loja, TipoLoja

class TestLojasTestCase(TestCase):
	fixtures = ['lojas.json']

	def setUp(self):
		super(TestLojasTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaBilBil(self):
		loja = Loja.objects.get(pk=1)
		self.assertEqual(loja.nome, 'BilBil Beer')

	def testNomeObrigatorio(self):
		with self.assertRaises(IntegrityError):
			loja = Loja.objects.create(nome=None, site='bilbilbeer.com.br', email='contato@bilbilbeer.com.br')

	def testSiteObrigatorio(self):
		with self.assertRaises(IntegrityError):
			loja = Loja.objects.create(nome='BilBil Beer', site=None, email='contato@bilbilbeer.com.br')

	def testEmailObrigatorio(self):
		with self.assertRaises(IntegrityError):
			loja = Loja.objects.create(nome='BilBil Beer', site='www.bilbilbeer.com.br', email=None)


class TestTipoLojasTestCase(TestCase):
	fixtures = ['tipo_loja.json']

	def setUp(self):
		super(TestTipoLojasTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaVendaInsumo(self):
		tipo_loja = TipoLoja.objects.get(pk=1)
		self.assertEqual(tipo_loja.nome, 'Venda de Insumos')

	def testNomeObrigatorio(self):
		with self.assertRaises(IntegrityError):
			tipo_loja = TipoLoja.objects.create(nome=None)