from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from .serializers import *
from .filters import *
from .models import *


class CityView(ListCreateAPIView):
    # queryset = CityModel.objects.all()
    serializer_class = CitySerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['name']

    def get_queryset(self):

        if hasattr(self.request.query_params, 'name'):
           q_para = dict()
           q_para['name'] = self.request.query_params.get('name')
           q_base = CityModel.objects.filter(map(q_para))
        else:
            q_base = CityModel.objects.all()

        return q_base


class StreetView(ListCreateAPIView):
    # queryset = StreetModel.objects.all()
    serializer_class = StreetSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['name', 'city']

    def get_queryset(self):

        if hasattr(self.request.query_params, 'name'):
           q_para = dict()
           q_para['name'] = self.request.query_params.get('name')
           q_base = StreetModel.objects.filter(map(q_para))
        else:
            q_base = StreetModel.objects.all()

        return q_base

class ShopView(ListCreateAPIView):
    # queryset = ShopModel.objects.all()
    serializer_class = ShopSerializer


    def get_queryset(self):
        q_para = dict()

        find_params = ['name', 'open']
        for f_param in find_params:
            if f_param in self.request.query_params.keys():
                q_para[f_param] = self.request.query_params.get(f_param)

        # сделаем вариативность для полей внешних ключей
        # если поиск по Id то ищем как есть
        # если значение строковое, занчит хотим искать по названиям
        find_params = ['street', 'city']
        for f_param in find_params:
            if f_param in self.request.query_params.keys():
                param_value = self.request.query_params.get(f_param)
                present_fild = '__name' if not param_value.isnumeric() else ''
                q_para[f_param + present_fild] = param_value
        if len(q_para) > 0:
            q_base = ShopModel.objects.filter(**q_para)
        else:
            q_base = ShopModel.objects.all()

        return q_base