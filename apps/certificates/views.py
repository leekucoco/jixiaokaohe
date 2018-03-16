
from django.contrib.auth import get_user_model

from rest_framework import viewsets

from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import Cerficates,IndexUserCertificate
from .serializers import  CerficateSerializer,IndexUserCertificateSerializer,IndexUserCertificateSerializer2
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend




class CerficatesPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class CerficatesViewset(viewsets.ModelViewSet):
    """
    机构
    """
    serializer_class = CerficateSerializer
    queryset = Cerficates.objects.all().order_by("id")
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )
    pagination_class = CerficatesPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name')
    ordering_fields = ('name', 'basesalary')
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


class IndexUserCertificatePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class IndexUserCertificateViewset(viewsets.ModelViewSet):
    """
    用户证书中间表
    """
    #serializer_class = IndexUserCertificateSerializer
    queryset = IndexUserCertificate.objects.all().order_by("id")
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )
    pagination_class = IndexUserCertificatePagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user__name','certificate__name')

    ordering_fields = ('user', 'certificate','add_time','update_time')

    def get_serializer_class(self):
        if self.action == "retrieve":
            return IndexUserCertificateSerializer
        elif self.action == "create":
            return IndexUserCertificateSerializer2

        return IndexUserCertificateSerializer

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