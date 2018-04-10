from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model

from rest_framework import viewsets

from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from datetime import time, datetime
from .models import CoefficientDetail
from .serializers import  CoefficientDetailSerializer,CofficientCreateSerializer,CofficientUpdateSerializer
from rest_framework import filters
from django_filters import rest_framework as drffilters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_extensions.cache.mixins import CacheResponseMixin
from depart.models import DepartDetail

class CoefficientDetailPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class CoefficientFilter(drffilters.FilterSet):
    min_coefficent = drffilters.NumberFilter(name="coefficent", lookup_expr='gte')
    max_coefficent = drffilters.NumberFilter(name="coefficent", lookup_expr='lte')
    #depart = drffilters.ModelChoiceFilter(queryset=DepartDetail.objects.all())
    update_time = drffilters.DateTimeFromToRangeFilter()
    class Meta:
        model = CoefficientDetail
        fields = ['user__name','user__idcardnumber', 'update_time', 'min_coefficent', 'max_coefficent']


class CoefficientDetailViewset(CacheResponseMixin,viewsets.ModelViewSet):
    """
    系数
    """
    #serializer_class = CoefficientDetailSerializer
    queryset = CoefficientDetail.objects.all().order_by("id")
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    pagination_class = CoefficientDetailPagination
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CoefficientFilter
    search_fields = ('user__name','user__idcardnumber','rank13demands__post__name',)
    ordering_fields = ('coefficent', 'rank','add_time','update_time')


    def perform_update(self, serializer):
        serializer.validated_data["update_time"] = datetime.now()
        serializer.save()

    def get_serializer_class(self):
        if self.action =="create":
            return CofficientCreateSerializer
        elif self.action =="list":
            return CoefficientDetailSerializer
        elif self.action == "retrieve":
            return CoefficientDetailSerializer
        elif self.action == "update":
            return CofficientUpdateSerializer
        else:
            return CofficientCreateSerializer
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return [permissions.IsAdminUser()]
        elif self.action == "list":
            return [permissions.IsAuthenticated()]
        elif self.action == "update":
            return [permissions.IsAdminUser()]
        elif self.action == "partial_update":
            return [permissions.IsAdminUser()]
        elif self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

