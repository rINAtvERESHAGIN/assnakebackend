from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
import assnake

from dataset.serializers import DataSetListInBD


# from api_front.serializers import IncomingDataSerializer
# from api_front.convert_data_for_elman.convert_phrase_to_numb import con_text_to_num
# from api_front.elman_main.elman_r_n_n import get_phrase_status


class Data(APIView):

    def get(self, request):
        print('-------------------IN-----------GET')
        all_values_of_dataset = assnake.Dataset.list_in_db().values()
        print(all_values_of_dataset)
        serializer = DataSetListInBD(all_values_of_dataset, many='True')
        return Response(serializer.data)
