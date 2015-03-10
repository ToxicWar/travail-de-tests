# coding: utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.db.models import fields
import yaml

FIELD_TYPE = {
    'int': fields.IntegerField,
    'char': fields.CharField,
    'text': fields.TextField,
    'date': fields.DateField
}

FIELD_DEFAULTS = {
    'char': {'max_length': 100},
    'text': {'max_length': 1000}
}


def get_field_by_type(_type, **kwargs):
    if _type in FIELD_DEFAULTS:
        kwargs.update(FIELD_DEFAULTS[_type])
    return FIELD_TYPE[_type](**kwargs)


def get_models_from_file(config_file=settings.MODELS_FILE):
    models = yaml.load(open(config_file, 'r'))

    for name, params in models.iteritems():
        fields = {}

        for field in params['fields']:
            kwargs = {'verbose_name': field['title'], 'blank': True, 'null': True}
            dynamic_field = {field['id']: get_field_by_type(field['type'], **kwargs)}
            fields.update(dynamic_field)

        yield {
            'name': name,
            'verbose_name': params['title'],
            'fields': fields
        }
