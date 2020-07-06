# from abc import ABC
from rest_framework import serializers


class IncomingDataSerializer(serializers.Serializer):
    df = serializers.CharField()


class DataSetListInBD(serializers.Serializer):
    # BIOCAD_WGS_CLEAN = serializers.DictField()
    data_type = serializers.CharField()
    description = serializers.DictField()
    df = serializers.CharField()
    fs_prefix = serializers.CharField()

