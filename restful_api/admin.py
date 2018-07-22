from django.contrib import admin
from django.apps import apps


app = apps.get_app_config('restful_api')

# register models to see them at admin/
for model_name, model in app.models.items():
    admin.site.register(model)
