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

def admin_generator(app_name, model_name):
    template = get_template('startcbv/admin.py')
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

def touch(fname, times = None):
    with file(fname, 'a'):
        os.utime(fname, times)

class Command(LabelCommand):
    print "Generating your app with class-based views..."

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
        target = open(app_name + "/urls.py", 'w')
        target.write(urls_generator(app_name, app_name.capitalize().rstrip("s")))
        target.close()
        target = open(app_name + "/views.py", 'w')
        target.write(views_generator(app_name, app_name.capitalize().rstrip("s")))
        target.close()
        target = open(app_name + "/admin.py", 'w')
        target.write(admin_generator(app_name, app_name.capitalize().rstrip("s")))
        target.close()

        touch(app_name + "/__init__.py")

        template_dir = 'templates/' + app_name
        os.makedirs(template_dir)
        target = open(template_dir + "/" + app_name.rstrip("s") + "_list.html", 'w')
        target.write(list_template_generator(app_name, app_name.capitalize().rstrip("s")))
        target.close()

        target = open(template_dir + "/" + app_name.rstrip("s") + "_detail.html", 'w')
        target.write(detail_template_generator(app_name, app_name.capitalize().rstrip("s")))
        target.close()

# TODO: rather than using rstrip to create the singular form from the plural, 
# use something like http://code.activestate.com/recipes/577781-pluralize-word-convert-singular-word-to-its-plural/
