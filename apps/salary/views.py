from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import mixins
from django.shortcuts import redirect
from rest_framework import permissions
from .serializers import SalaryRecordSerializer,FSlarySerializer
from utils.permissions import IsOwnerOrReadOnly
from .models import SalaryRecord,FSalary
from django.contrib.auth import get_user_model
from utils.permissions import IsOwnerOrReadOnly
User = get_user_model()
from .task import createsalaryrecord,destroysalaryrecord
class SalaryRecordViewset(viewsets.ModelViewSet):
    """
    工资记录操作
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = SalaryRecordSerializer
    #lookup_field = "goods_id"

    def perform_create(self, serializer):
        salaryrecord = serializer.save()
        createsalaryrecord.delay(salaryrecord)

    def perform_destroy(self, instance):
        # goods = instance.goods
        # goods.goods_num += instance.nums
        # goods.save()
        #instance.delete()
        destroysalaryrecord.delay(instance)
    #
    # def perform_update(self, serializer):
    #     existed_record = SalaryRecord.objects.get(id=serializer.instance.id)
    #     existed_nums = existed_record.nums
    #     saved_record = serializer.save()
    #     nums = saved_record.nums-existed_nums
    #     goods = saved_record.goods
    #     goods.goods_num -= nums
    #     goods.save()

    def get_serializer_class(self):
        # if self.action == 'list':
        #     return SalaryRecordSerializer
        # else:
        #     return SalaryRecordSerializer
        return SalaryRecordSerializer
    def get_queryset(self):
        return SalaryRecord.objects.filter(user=self.request.user)

    def get_permissions(self):
        return [permissions.IsAdminUser()]
        # if self.action == "retrieve":
        #     return [permissions.IsAuthenticated()]
        # elif self.action == "create":
        #     return [permissions.IsAdminUser()]
        # elif self.action == "list":
        #     return [permissions.IsAuthenticated()]
        # elif self.action == "update":
        #     return [permissions.IsAdminUser()]
        # elif self.action == "partial_update":
        #     return [permissions.IsAdminUser()]
        # elif self.action == "destroy":
        #     return [permissions.IsAdminUser()]
        # else:
        #     return [permissions.IsAuthenticatedOrReadOnly()]

class FSalaryViewset(viewsets.ModelViewSet):
    """
    福利薪酬明细
    """
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = FSlarySerializer
    def get_queryset(self):
        #return FSalary.objects.filter(user=self.request.user)
        if self.request.user.is_staff:
            return FSalary.objects.all()
        else:
            return FSalary.objects.filter(user=self.request.user)
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
            return [permissions.IsAuthenticated()]