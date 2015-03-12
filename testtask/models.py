# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from .utils import get_models_from_file


class DynamicModelManager(models.Manager):
    def __init__(self, model, instance=None):
        super(DynamicModelManager, self).__init__()
        self.model = model
        self.instance = instance

    def get_queryset(self):
        if self.instance is None:
            return super(DynamicModelManager, self).get_queryset()

        _filter = {self.instance._meta.pk.name: self.instance.pk}
        return super(DynamicModelManager, self).get_queryset().filter(**_filter)


class DynamicModelDescriptor(object):
    def __init__(self, model):
        self.model = model

    def __get__(self, instance):
        if instance is None:
            return DynamicModelManager(self.model)
        return DynamicModelManager(self.model, instance)


class DynamicModel(object):
    registry = {}

    def contribute_to_class(self, cls, name):
        self.manager_name = name
        models.signals.class_prepared.connect(self.finalize, sender=cls)

    def finalize(self, sender, **kwargs):
        models_dict = get_models_from_file()

        for model in models_dict:
            dynamic_model = self.create_dynamic_model(model)
            descriptor = DynamicModelDescriptor(dynamic_model)
            setattr(sender, self.manager_name, descriptor)

    def create_dynamic_model(self, model=None):
        """
        Create a dynamic model from dict data.
        """
        if not model:
            return None

        attrs = self.get_dynamic_model_fields(model)
        # byte string looks sad
        attrs.update(Meta=type(b'Meta', (), self.get_meta_fields(model)))
        name = b'{}DynamicModel'.format(model['name'].title())
        dynamic_model = type(name, (models.Model,), attrs)
        self.__class__.registry[name] = dynamic_model
        return dynamic_model

    def __contains__(self, module_name):
        return module_name in self.__class__.registry

    def get_dynamic_model(self, module_name):
        return self.__class__.registry.get(module_name, None)

    def get_dynamic_model_fields(self, model=None):
        fields = {
            'id': models.AutoField(primary_key=True),
            '__module__': self.__module__,
            '__unicode__': lambda x: u'#{} - {}'.format(x.id, model['name'])
        }
        fields.update(model['fields'])
        return fields

    def get_meta_fields(self, model=None):
        return {
            'ordering': ('-id',),
            'verbose_name': unicode(model['verbose_name'] if model else 'Name'),
            'verbose_name_plural': unicode(model['verbose_name'] if model else 'Names'),
        }


class Model(models.Model):
    models = DynamicModel()
