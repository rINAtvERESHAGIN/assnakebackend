from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

from api_front.serializers import IncomingDataSerializer


# class Data(APIView):
#
#     def post(self, request):
#         serializer = IncomingDataSerializer(data=request.data)
#         if serializer.is_valid():
#             # start_log(serializer.data, table_name)
#             # передаем данные в метод по конвертации
#             # передаем полученные данные в нейронную сеть и ждем ответа
#             return JsonResponse(data={'status': 'Got'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
