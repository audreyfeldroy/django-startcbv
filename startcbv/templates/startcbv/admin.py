from django.contrib import admin

from {{ app_name }}.models import {{ model_name }}

class {{ model_name }}Admin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pub_date')
    fields = ['name', 'slug', 'pub_date']
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    search_fields = ['name']

admin.site.register({{ model_name }}, {{ model_name }}Admin)
