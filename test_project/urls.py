from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # The appropriate URL pattern for your app should be placed here manually AFTER
    #  you've run 'python manage.py startcbv things'
    # url(r'^things/', include('things.urls')),
)
