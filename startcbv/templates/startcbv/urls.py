from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from {{ app_name }}.models import {{ model_name }}

urlpatterns = patterns('{{ app_name }}.views',
    url(regex=r'^$',
        view=ListView.as_view(
            queryset={{ model_name }}.objects.order_by('-pub_date'),
            context_object_name='latest_{{ model_name.lower }}_list',
            template_name='{{ app_name }}/{{ model_name.lower }}_list.html'),
        name='{{ model_name.lower }}_list',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(
            model={{ model_name }},
            template_name='{{ app_name }}/{{ model_name.lower }}_detail.html'),
        name='{{ model_name.lower }}_detail',
    ),
)
