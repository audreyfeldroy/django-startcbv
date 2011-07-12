import os, string

from django.core.management.base import copy_helper, CommandError, LabelCommand
from django.utils.importlib import import_module

from django.template import Context
from django.template.loader import get_template

def models_generator(app_name, model_name):
    template = get_template('startcbv/models.py')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

def urls_generator(app_name, model_name):
    template = get_template('startcbv/urls.py')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

def views_generator(app_name, model_name):
    template = get_template('startcbv/views.py')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

def list_template_generator(app_name, model_name):
    template = get_template('startcbv/_list.html')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

def detail_template_generator(app_name, model_name):
    template = get_template('startcbv/_detail.html')
    c = Context({'model_name': model_name,
                 'app_name': app_name})
    return template.render(c)

class Command(LabelCommand):
    print "startcbv blah"

    def handle_label(self, app_name, directory=None, **options):
        print app_name
        os.makedirs(app_name)
#        print models_generator(app_name, app_name.capitalize().rstrip("s"))
#        print urls_generator(app_name, app_name.capitalize().rstrip("s"))
#        print views_generator(app_name, app_name.capitalize().rstrip("s"))
#        print list_template_generator(app_name, app_name.capitalize().rstrip("s"))
#        print detail_template_generator(app_name, app_name.capitalize().rstrip("s"))
        target = open(app_name + "/models.py", 'w')
        target.write(models_generator(app_name, app_name.capitalize().rstrip("s")))
        target.close()

# TODO: rather than using rstrip to create the singular form from the plural, 
# use something like http://code.activestate.com/recipes/577781-pluralize-word-convert-singular-word-to-its-plural/
