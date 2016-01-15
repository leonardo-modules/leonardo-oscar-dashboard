
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_oscar_dashboard.Config'


LEONARDO_APPS = ['leonardo_oscar_dashboard']

LEONARDO_PLUGINS = [
    ('leonardo_store.apps.dashboard', _('Store: Dashboard'),),
]


class Config(AppConfig):
    name = 'leonardo_oscar_dashboard'
    verbose_name = "leonardo-oscar-dashboard"
