import os, string

from django.core.management.base import copy_helper, CommandError, LabelCommand
from django.utils.importlib import import_module

from django.template import Context
from django.template.loader import get_template

def model_generator(app_name, model_name):
    template = get_template('startcbv/models.py')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

def urls_generator(app_name, model_name):
    template = get_template('startcbv/urls.py')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

class Command(LabelCommand):
    print "startcbv blah"

    def handle_label(self, app_name, directory=None, **options):
        print app_name
#        print model_generator(app_name, app_name.capitalize())
        print urls_generator(app_name, app_name.capitalize())



