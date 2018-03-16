# -*- coding: utf-8 -*-
__author__ = 'bobby'
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime,date
from .models import Cerficates,IndexUserCertificate
class CerficateSerializer(serializers.ModelSerializer):
    # certificate_user= serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='indexusercertificate-detail'
    # )
    class Meta:
        model = Cerficates
        fields = ('name','score',)

class IndexUserCertificateSerializer(serializers.ModelSerializer):
    certificate = serializers.StringRelatedField()
    class Meta:
        model = IndexUserCertificate
        fields = ("user", "certificate", "image")

class IndexUserCertificateSerializer2(serializers.ModelSerializer):

    class Meta:
        model = IndexUserCertificate
        fields = ("user", "certificate", "image")

    # def create(self, validated_data):
    #     certificates_data = validated_data.pop('certificate')
    #     name = certificates_data['name']
    #     certificateres = Cerficates.objects.filter(name=name)
    #     if certificateres:
    #         validated_data["certificate"] = certificateres[0]
    #         indexusercertificate = IndexUserCertificate.objects.create(**validated_data)
    #         return indexusercertificate
    #     else:
    #         certificateres = Cerficates.objects.create(**certificates_data)
    #         validated_data["certificate"] = certificateres
    #         indexusercertificate = IndexUserCertificate.objects.create(**validated_data)
    #         return indexusercertificate
    #     # for certificate_data in certificates_data:
    #     #return indexusercertificate
    # # def create(self, request, *args, **kwargs):
    # #     serializer = self.get_serializer(data=request.data)
    # #     serializer.is_valid(raise_exception=True)
    # #     self.perform_create(serializer)
    # #     headers = self.get_success_headers(serializer.data)
    # #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # #
    # # def perform_create(self, serializer):
    # #     serializer.save()
    #
    def update(self, instance, validated_data):
        #修改商品数量
        instance.update_time = datetime.now()
       # certificates_data = validated_data.pop('certificate')
       # certificateres = Cerficates.objects.update(**certificates_data)
       # validated_data["certificate"] = certificateres
        instance.save()
        return instance
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)
    #
    # def perform_update(self, serializer):
    #     serializer.save()
    #
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)


    # def create(self, validated_data):
    #     user = self.context["request"].user
    #     image = validated_data["image"]
    #     certificateinfo = validated_data["certificate"]
    #     existed = Cerficates.objects.filter(certificate=certificateinfo)
    #     if existed:
    #         indexusercertificateins = IndexUserCertificate.objects.create(**validated_data)
    #
    #         return "already exist"
    #     else:
    #         existed = Cerficates.objects.create(**validated_data)
    #         indexusercertificateins = IndexUserCertificate.objects.create(**validated_data)
    #     return indexusercertificateins
    #
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
    # def update(self, instance, validated_data):
    #     #修改商品数量
    #     instance.nums = validated_data["nums"]
    #     instance.save()
    #     return instance