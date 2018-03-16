# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import DepartDetail,IndexUserDepart
class DepartSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartDetail
        fields = ("name", "dept_type", "basesalary")

class IndexUserDepartSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndexUserDepart
        fields = "__all__"