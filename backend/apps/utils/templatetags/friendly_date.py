from django import template
import utils.friendly_dates as fd_utils

register = template.Library()


@register.simple_tag
def friendly_date(time=False):
    return fd_utils.friendly_date(time)
