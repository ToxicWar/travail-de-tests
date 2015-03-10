# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HobbiesDynamicModel',
            fields=[
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': '\u0425\u043e\u0431\u0431\u0438',
                'verbose_name_plural': '\u0425\u043e\u0431\u0431\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomsDynamicModel',
            fields=[
                ('department', models.CharField(max_length=100, null=True, verbose_name='\u041e\u0442\u0434\u0435\u043b', blank=True)),
                ('spots', models.IntegerField(null=True, verbose_name='\u0412\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c', blank=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': '\u041a\u043e\u043c\u043d\u0430\u0442\u044b',
                'verbose_name_plural': '\u041a\u043e\u043c\u043d\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsersDynamicModel',
            fields=[
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('paycheck', models.IntegerField(null=True, verbose_name='\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430', blank=True)),
                ('date_joined', models.DateField(null=True, verbose_name='\u200b\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443', blank=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
    ]
