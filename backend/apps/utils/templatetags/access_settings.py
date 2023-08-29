from django import template
from django.conf import settings

register = template.Library()

if hasattr(settings, 'TEMPLATE_ACCESSIBLE_SETTING_VARS'):
    ALLOWABLE_VALUES = settings.TEMPLATE_ACCESSIBLE_SETTING_VARS
else:
    ALLOWABLE_VALUES = ('DEBUG',)


@register.assignment_tag
def settings_value(name):
    if name in ALLOWABLE_VALUES:
        return getattr(settings, name, '')
    return ''
