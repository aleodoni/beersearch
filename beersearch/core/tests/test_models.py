# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock, Mock
from django.db import IntegrityError, DataError

from ..models import Loja, TipoLoja, FabricaMalte, Malte, Lupulo, FabricaFermento, Fermento

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

class TestFabricaMalteTestCase(TestCase):
	fixtures = ['fabrica_malte.json']

	def setUp(self):
		super(TestFabricaMalteTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaFabricaMalte(self):
		fabrica_malte = FabricaMalte.objects.get(pk=1)
		self.assertEqual(fabrica_malte.nome, 'Weynermann')

	def testNomeObrigatorio(self):
		with self.assertRaises(IntegrityError):
			fabrica_malte = FabricaMalte.objects.create(nome=None, pais='Alemanha')			

	def testPaisObrigatorio(self):
		with self.assertRaises(IntegrityError):
			fabrica_malte = FabricaMalte.objects.create(nome='Weinermann', pais=None)			

class TestMalteTestCase(TestCase):
	fixtures = ['fabrica_malte.json', 'malte.json']

	def setUp(self):
		super(TestMalteTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaMaltePilsenWeynermann(self):
		malte = Malte.objects.get(pk=1)
		self.assertEqual(malte.nome, 'Pilsen')

	def testInsereMalteOK(self):
		fabrica_malte = FabricaMalte.objects.get(pk=1)
		malte = Malte.objects.create(nome='Pilsen', fabrica=fabrica_malte, ebc=3.5)

	def testInsereMalteFabricaNula(self):
		with self.assertRaises(IntegrityError):
			malte = Malte.objects.create(nome='Pilsen', fabrica=None, ebc=3.5)

	def testInsereMalteEbcNula(self):
		fabrica_malte = FabricaMalte.objects.get(pk=1)
		with self.assertRaises(IntegrityError):
			malte = Malte.objects.create(nome='Pilsen', fabrica=fabrica_malte, ebc=None)

class TestLupuloTestCase(TestCase):
	fixtures = ['lupulo.json']

	def setUp(self):
		super(TestLupuloTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaLupuloCascade(self):
		lupulo = Lupulo.objects.get(pk=1)
		self.assertEqual(lupulo.nome, 'Cascade')

	def testInsereLupuloOK(self):
		lupulo = Lupulo.objects.create(nome='Cascade', tipo=1)

	def testInsereLupuloTipoNulo(self):
		with self.assertRaises(IntegrityError):
			lupulo = Lupulo.objects.create(nome='Amarillo', tipo=None)

	def testInsereLupuloNomeNulo(self):
		with self.assertRaises(IntegrityError):
			lupulo = Lupulo.objects.create(nome=None, tipo=1)			

class TestFabricaFermentoTestCase(TestCase):
	fixtures = ['fabrica_fermento.json']

	def setUp(self):
		super(TestFabricaFermentoTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaFabricaLesaffre(self):
		fabrica_fermento = FabricaFermento.objects.get(pk=1)
		self.assertEqual(fabrica_fermento.nome, 'Lesaffre')

	def testInsereFabricaFermentoOK(self):
		fabrica_fermento = FabricaFermento.objects.create(nome='Lesaffre')

	def testInsereFabricaFermentoNomeNulo(self):
		with self.assertRaises(IntegrityError):
			fabrica_fermento = FabricaFermento.objects.create(nome=None)

class TestFermentoTestCase(TestCase):
	fixtures = ['fabrica_fermento.json', 'fermento.json']

	def setUp(self):
		super(TestFermentoTestCase, self).setUp()

	def testDummy(self):
		self.assertEqual(1, 1)

	def testRetornaFermentoUS05(self):
		fermento = Fermento.objects.get(pk=1)
		self.assertEqual(fermento.nome, 'Fermentis US-05')

	def testInsereMalteOK(self):
		fabrica_fermento = FabricaFermento.objects.get(pk=1)
		fermento = Fermento.objects.create(nome='Fermentis Us-05', fabrica=fabrica_fermento, tipo=1)

	def testInsereFermentoFabricaNula(self):
		with self.assertRaises(IntegrityError):
			fermento = Fermento.objects.create(nome='Fermentis US-05', fabrica=None, tipo=1)

	def testInsereFermentoTipoNulo(self):
		fabrica_fermento = FabricaFermento.objects.get(pk=1)
		with self.assertRaises(IntegrityError):
			fermento = Fermento.objects.create(nome='Fermentis US-05', fabrica=fabrica_fermento, tipo=None)			