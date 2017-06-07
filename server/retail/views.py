# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import viewsets

from .models import Chain, Store, Employee
from .serializers import ChainSerializer, StoreSerializer, EmployeeSerializer


# Create your views here.
class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# EOF
