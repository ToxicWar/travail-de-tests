# coding: utf-8
from __future__ import unicode_literals
from django.db.models import fields
from django.test import TestCase
from testtask.utils import get_field_by_type, get_models_from_file


class UtilsTests(TestCase):
    def test_get_field_by_type(self):
        int_field = get_field_by_type('int')
        char_field = get_field_by_type('char')
        text_field = get_field_by_type('text')
        date_field = get_field_by_type('date')

        self.assertIsInstance(int_field, fields.IntegerField)
        self.assertIsInstance(char_field, fields.CharField)
        self.assertIsInstance(text_field, fields.TextField)
        self.assertIsInstance(date_field, fields.DateField)

    def test_get_models_from_file(self):
        models = [item for item in get_models_from_file()]
        model = models[0]

        self.assertEqual(len(models), 3)
        self.assertEqual(model.keys(), ['fields', 'verbose_name', 'name'])

    def test_dummy_get_models_from_file(self):
        models = [item for item in get_models_from_file(config_file='')]

        self.assertEqual(models, [])
