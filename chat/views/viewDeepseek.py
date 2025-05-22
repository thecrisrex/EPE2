from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat.services.deep_seek_service import DeepSeekService
from chat.serializers import DeepSeekInputSerializer

class DeepSeekView(APIView):
    def post(self, request):
        serializer = DeepSeekInputSerializer(data=request.data)
        if serializer.is_valid():
            try:
                analysis = DeepSeekService().analyze(serializer.validated_data)
                return Response({"analysis": analysis}, status=status.HTTP_200_OK)
            except Exception as e:
                print("❌ ERROR INTERNO:", str(e))  # <--- DEBUG
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)