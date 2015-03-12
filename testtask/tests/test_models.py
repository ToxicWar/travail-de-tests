# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
from testtask.models import DynamicModel, DynamicModelDescriptor
from testtask.utils import get_models_from_file


class ModelTests(TestCase):
    def setUp(self):
        self.model = {'fields': {'test': models.CharField('test', max_length=10)},
                 'verbose_name': 'Test', 'name': 'tests'}
        self.model_name = b'TestsDynamicModel'
        self.dummy = DynamicModel()

    def test_check_dynamic_model(self):
        Model = DynamicModel.registry['HobbiesDynamicModel']
        dummy = Model()

        self.assertEqual(len(DynamicModel.registry), 3)
        self.assertEqual(Model._meta.verbose_name, 'Хобби')
        self.assertTrue(hasattr(dummy, 'title'))
        self.assertTrue(hasattr(dummy, 'description'))
        self.assertFalse(hasattr(dummy, 'name'))

    def test_dummy_create_dynamic_model(self):
        Model = self.dummy.create_dynamic_model()

        self.assertIsNone(Model)
        self.assertEqual(len(DynamicModel.registry), 3)

    def test_create_post(self):
        self.assertEqual(len(DynamicModel.registry), 3)

        NewModel = self.dummy.create_dynamic_model(self.model)

        self.assertEqual(NewModel, DynamicModel.registry[self.model_name])
        self.assertEqual(len(DynamicModel.registry), 4)

        DynamicModel.registry.pop('TestsDynamicModel', None)

    def test_get_dynamic_model_fields(self):
        fields = self.dummy.get_dynamic_model_fields(self.model)

        self.assertIn('id', fields)
        self.assertIn('__unicode__', fields)

    def test_get_meta_fields(self):
        meta_fields = self.dummy.get_meta_fields(self.model)
        dummy_fields = self.dummy.get_meta_fields()

        self.assertIn('ordering', meta_fields)
        self.assertIn('verbose_name', meta_fields)
        self.assertEqual(meta_fields['verbose_name'], 'Test')
        self.assertIn('ordering', dummy_fields)
        self.assertIn('verbose_name', dummy_fields)
        self.assertEqual(dummy_fields['verbose_name'], 'Name')

    def test_get_dynamic_model(self):
        Model = DynamicModel.registry['HobbiesDynamicModel']
        Model2 = self.dummy.get_dynamic_model('HobbiesDynamicModel')

        self.assertEqual(Model, Model2)

    def test_contains(self):
        self.assertTrue('HobbiesDynamicModel' in self.dummy)
        self.assertFalse('Dummy' in self.dummy)
