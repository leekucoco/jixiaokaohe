from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model

from rest_framework import viewsets

from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import CoefficientDetail
from .serializers import  CoefficientDetailSerializer,CofficientCreateSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend




class CoefficientDetailPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class CoefficientDetailViewset(viewsets.ModelViewSet):
    """
    系数
    """
    #serializer_class = CoefficientDetailSerializer
    queryset = CoefficientDetail.objects.all().order_by("id")
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )
    pagination_class = CoefficientDetailPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user__name','user__idcardnumber')
    ordering_fields = ('coefficent', 'rank','add_time','update_time')
    def get_serializer_class(self):
        if self.action =="create":
            return CofficientCreateSerializer
        elif self.action =="list":
            return CoefficientDetailSerializer
        elif self.action == "retrieve":
            return CoefficientDetailSerializer
        else:
            return CofficientCreateSerializer
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticatedOrReadOnly()]
        elif self.action == "create":
            return [permissions.IsAdminUser()]
        elif self.action == "list":
            return [permissions.IsAuthenticatedOrReadOnly()]
        elif self.action == "update":
            return [permissions.IsAdminUser()]
        elif self.action == "partial_update":
            return [permissions.IsAdminUser()]
        elif self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

