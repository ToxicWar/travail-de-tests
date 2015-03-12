#!/usr/bin/env bash
pushd . > /dev/null
curdir=$(dirname "$0")
cd $curdir
curdir=$(pwd)
updir=$(dirname $(dirname $curdir))
popd > /dev/null
export PYTHONPATH=$updir:$PYTHONPATH
export DJANGO_SETTINGS_MODULE="testtask.tests.settings"
django-admin.py test testtask $@
