# coding: utf-8
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.db.models.loading import get_model
from django.test import TestCase
import json


class ViewsTests(TestCase):
    fixtures = ['test_data']

    def test_task_view_200(self):
        response = self.client.get(reverse_lazy('TestTask'))

        self.assertTrue('models' in response.context)
        self.assertTrue(len(response.context['models']), 3)
        self.assertEqual(response.status_code, 200)

    def test_get_model_data_200(self):
        response = self.client.get(reverse_lazy('ModelData', kwargs={'model_name': 'HobbiesDynamicModel'}))

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertTrue('fields' in data)
        self.assertTrue('qs' in data)
        self.assertEqual(len(data['fields']), len(data['qs'][0]))

    def test_get_model_data_400(self):
        response = self.client.get(reverse_lazy('ModelData', kwargs={'model_name': 'SomeModel'}))
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in data)
        self.assertEqual(data['error'], "App 'testtask' doesn't have a 'somemodel' model.")

    def test_update_model_data_200(self):
        data = 'field={}&id={}&data={}'.format('title', 1, 'Test')
        response = self.client.put(reverse_lazy('ModelData', kwargs={'model_name': 'HobbiesDynamicModel'}), data=data)
        status = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('status' in status)
        self.assertEqual(status['status'], 'ok')

    def test_update_model_data_200_error(self):
        data = 'field={}&id={}&data={}'.format('date_joined', 1, 'dummy')
        response = self.client.put(reverse_lazy('ModelData', kwargs={'model_name': 'UsersDynamicModel'}), data=data)
        status = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('status' in status)
        self.assertEqual(status['status'], 'error')
        self.assertTrue('message' in status)

    def test_update_model_data_400(self):
        data = 'field={}&id={}&data={}'.format('title', 1, 'Test')
        response = self.client.put(reverse_lazy('ModelData', kwargs={'model_name': 'SomeModel'}), data=data)
        status = json.loads(response.content)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in status)
        self.assertEqual(status['error'], "App 'testtask' doesn't have a 'somemodel' model.")
