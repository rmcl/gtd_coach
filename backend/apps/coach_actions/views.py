from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from coach_actions.service import get_gtd_coach_service

class CoachView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get('message', None)
        target_number_id = request.data.get('target_number_id', None)

        if not user_message:
            return JsonResponse({'error': 'message is required'})

        if not target_number_id:
            return JsonResponse({'error': 'target_number_id is required'})

        coach_service = get_gtd_coach_service()

        coach_response = coach_service.invoke(target_number_id, user_message)
        return JsonResponse({'response': coach_response})
