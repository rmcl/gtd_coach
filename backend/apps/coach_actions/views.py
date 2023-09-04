from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from coach_actions.service import get_gtd_coach_service

class CoachView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get('message')

        coach_service = get_gtd_coach_service()

        coach_response = coach_service.invoke(user_message)
        return JsonResponse({'response': coach_response})
