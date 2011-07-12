===============
django-startcbv
===============

Installation
------------

TODO: package this up.  At some point it will be::

    Add django-startcbv==0.1 to requirements.txt
    pip install -r requirements.txt

Usage
-----

For all of the following steps, replace "things" with the name of the app that you wish to create::

    python manage.py startcbv things

Add your "things" app to INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'things',
    )

Add your "things" app URL pattern to urls.py::

    url(r'^things/', include('things.urls')),

Then::

    python manage.py syncdb
    python manage.py runserver
