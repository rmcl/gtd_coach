from django.views.generic import View
from django.http import JsonResponse
from django.utils.text import slugify
from django.urls import reverse
from allauth.account.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin


class PasswordChangeView(
    LoginRequiredMixin,
    PasswordChangeView
):

    def get_success_url(self):
        # user changed passoword, set password_change_required flag to False
        user = self.request.user
        user.password_change_required = False
        user.save()
        return reverse('setup')
