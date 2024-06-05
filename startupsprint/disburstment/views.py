from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import check_for_upcoming_installments




class EMIReminder(APIView):
    def get(self, request, *args, **kwargs):
        # Trigger the Celery task
        result = check_for_upcoming_installments.delay()
        
        
        return Response({
            'status': 'success',
            'message': 'EMI reminder task has been triggered.',
            'task_id': result.id
        }, status=status.HTTP_200_OK)
