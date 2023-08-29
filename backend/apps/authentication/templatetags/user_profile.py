from django import template

register = template.Library()


@register.inclusion_tag('accounts/_profile.html')
def show_user_profile(user_account):
    return {
        'account': user_account
    }
