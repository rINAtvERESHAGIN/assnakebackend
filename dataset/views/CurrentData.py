from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse

from rest_framework import status

import assnake

from dataset.serializers import IncomingDataSerializer


class CurrentData(APIView):
    def post(self, request):
        serializer = IncomingDataSerializer(data=request.data)
        if serializer.is_valid():
            phrase_data = assnake.Dataset(serializer.data)
            print(phrase_data)
            return JsonResponse(data={'status': phrase_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
