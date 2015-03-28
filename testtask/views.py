# coding: utf-8
from __future__ import unicode_literals
from django.db.models.loading import get_model
from django.http import HttpResponse, HttpResponseBadRequest, QueryDict
from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from .models import DynamicModel
import logging
import json

logger = logging.getLogger(__name__)


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
        try:
            Model = get_model('testtask', model_name)
        except LookupError as e:
            logger.exception(e)
            return HttpResponseBadRequest(json.dumps({'error': e.message}))

        fields = [f.name for f in Model._meta.fields]
        qs = Model.objects.all().values_list(*fields)
        result = {'fields': fields, 'qs': list(qs)}
        return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder),
                            content_type='application/json')

    def put(self, request, model_name):
        try:
            Model = get_model('testtask', model_name)
        except LookupError as e:
            logger.exception(e)
            return HttpResponseBadRequest(json.dumps({'error': e.message}))

        data = QueryDict(request.body)
        field = data.get('field', None)
        _id = data.get('id', None)
        value = data.get('data', None)
        obj = Model.objects.get(pk=_id)
        setattr(obj, field, value)

        try:
            obj.save()
            data = {'status': 'ok'}
        except Exception as e:
            data = {'status': 'error', 'message': '{}'.format(e.message)}

        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder),
                            content_type='application/json')
model_data = csrf_exempt(ModelDataView.as_view())
