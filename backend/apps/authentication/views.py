from django.views.generic import View
from django.http import JsonResponse
from authentication.forms import DomainAvailabilityForm
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
        return reverse_lazy('setup')


# return domain availability
class DomainAvailabilityView(View):

    def get(self, request, **kwargs):
        form = DomainAvailabilityForm(request.GET)

        if form.is_valid():
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})


# slugify business names or anything else
class SlugifyView(View):

    def get(self, request, **kwargs):
        response = {
            'success': False
        }
        text = request.GET.get('text', None)
        if text is None or len(text) > 50:
            return JsonResponse(response)
        else:
            return JsonResponse({
                'success': True,
                'slug': slugify(text)
            })
