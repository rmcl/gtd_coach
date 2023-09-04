from django.urls import path
from coach_actions.views import CoachView

urlpatterns = [
    path('', CoachView.as_view(), name='coach_view'),
]