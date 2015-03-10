# coding: utf-8
from __future__ import unicode_literals
from django.db.models.loading import get_model
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.serializers.json import DjangoJSONEncoder
from .models import DynamicModel
import json


class TestTaskView(TemplateView):
    template_name = 'testtask.html'

    def get_context_data(self, **kwargs):
        context = super(TestTaskView, self).get_context_data(**kwargs)
        models = [{'id': _id, 'title': model._meta.verbose_name} for _id, model in DynamicModel.registry.iteritems()]
        context.update({
            'models': models
        })
        return context
testtask = TestTaskView.as_view()


class ModelDataView(View):
    def get(self, request, model_name):
        Model = get_model('testtask', model_name)
        fields = [f.name for f in Model._meta.fields]
        qs = Model.objects.all().values_list(*fields)
        result = {'fields': fields, 'qs': list(qs)}
        return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), content_type='application/json')
model_data = ModelDataView.as_view()
