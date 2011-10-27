=====
Usage
=====

Create a base.html template in templates/base.html.  It should contain a title and a content block, like this::

    <html>
    <head>
    <title>
    {% block title %}{% endblock %}
    </title>
    </head>

    <body>
    {% block content %}{% endblock %}
    </body>
    </html>

Add the "startcbv" app to INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'startcbv',
    )

For all of the following steps, replace "things" with the name of the app that you wish to create::

    python manage.py startcbv things

If you're done using startcbv, you can remove it from INSTALLED_APPS now; otherwise, leave it in to create more class-based view apps.  Add your "things" app to INSTALLED_APPS in settings.py.::

    INSTALLED_APPS = (
        ...
        'things',
    )

Add your "things" app URL pattern to urls.py::

    url(r'^things/', include('things.urls')),

Then::

    python manage.py syncdb
    python manage.py runserver
