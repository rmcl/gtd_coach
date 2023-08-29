"""Define a custom user model."""
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, BaseUserManager




class UserManager(BaseUserManager):
    """Custom User manager class."""


    def _create_user(
        self,
        email,
        first_name,
        last_name,
        password,
        is_staff,
        is_superuser,
        **extra_fields
    ):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(email, first_name, last_name, password,
                                 False, False, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        print('HI', email, first_name, last_name, password, extra_fields)
        return self._create_user(email, first_name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """

    USER = 'u'
    OWNER = 'o'

    ROLE_CHOICES = (
        (USER, 'user'),
        (OWNER, 'owner')
    )

    id = models.AutoField(primary_key=True)
    email = models.EmailField('E-mail address', max_length=254, unique=True)
    first_name = models.CharField('First name', max_length=40, blank=False, null=False)
    last_name = models.CharField('Last name', max_length=40, blank=False, null=False)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. Unselect '
            'this instead of deleting accounts.'))

    password_change_required = models.BooleanField(
        default=False,
        help_text='Used for invitation of team members when a temporary password is sent.')

    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    updated_at = models.DateTimeField('last updated', auto_now=True)
    last_login = models.DateTimeField('Last login', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    index_together = [
        ["is_active"],
    ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        """Display the user's email."""
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def get_short_name(self):
        "Returns the short name for the user."
        return f"{self.first_name} {self.last_name[0].upper()}"

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
