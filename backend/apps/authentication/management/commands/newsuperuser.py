from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.core import exceptions
from django.utils.text import slugify


# Allow creation of superuser with organization
class Command(BaseCommand):
    help = 'Used to create a superuser'
    requires_migrations_checks = True

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def get_input_data(self, field, message, default=None):
        """
        Override this method if you want to customize data inputs or
        validation exceptions.
        """
        val = ''
        raw_value = input(message)
        if default and raw_value == '':
            raw_value = default

        val = field.clean(raw_value, None)
        return val
