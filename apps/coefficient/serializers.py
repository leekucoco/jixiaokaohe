# -*- coding: utf-8 -*-
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime,date
from .models import CoefficientDetail
from depart.models import DepartDetail,IndexUserDepart
from depart.serializers import DepartSerializer
from users.serializers import UserDetailSerializer
from rest_framework import status
from rest_framework.response import Response
from certificates.models import IndexUserCertificate
from certificates.serializers import IndexUserCertificateSerializer
from users.models import UserProfile
User = get_user_model()


class CofficientCreateSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())
    class Meta:
        model = CoefficientDetail
        fields = "__all__"
    # def create(self, validated_data):
    #     user_data = validated_data['user']
    #     #name = certificates_data['name']
    #     user = CoefficientDetail.objects.filter(user_id=user_data.id)
    #     if user:
    #         coefficient = CoefficientDetail.objects.get(user_id=user_data.id)
    #         #return coefficient
    #         #headers = self.get_success_headers(coefficient)
    #         return "no exist"
    #     else:
    #         coefficient = CoefficientDetail.objects.create(**validated_data)
    #         return coefficient
    # def create(self, request, *args, **kwargs):
    #     user_data = request['user']
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     headers = self.get_success_headers(serializer.data)
    #     user = CoefficientDetail.objects.filter(user_id=user_data.id)
    #     if user:
    #         return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED, headers=headers)
    #     else:
    #         self.perform_create(serializer)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()

class CoefficientDetailSerializer(serializers.ModelSerializer):
    # certificate_user= serializers.HyperlinkedRelatedField(
    #     many=False,
    #     read_only=True,
    #     view_name='indexusercertificate-detail'
    # )
    #user = UserDetailSerializer(read_only=True)
    #user = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all(),read_only=True)
    #user = serializers.PrimaryKeyRelatedField(read_only=True)
    ra = serializers.SerializerMethodField()
    idcardnumber = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    depart = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    rank13 = serializers.SerializerMethodField()
    joinedyears = serializers.SerializerMethodField()
    yearsofwork = serializers.SerializerMethodField()
    scoreofyears = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    yearsofscore = serializers.SerializerMethodField()
    demandyears = serializers.SerializerMethodField()
    certificates = serializers.SerializerMethodField()
    certificatetotalscore = serializers.SerializerMethodField()
    class Meta:
        model = CoefficientDetail
        fields = ("id","user","coefficent","ra",
                  "name","idcardnumber","depart",
                  "post","rank13","joinedyears",
                  "yearsofwork","scoreofyears",
                  "education","yearsofscore","demandyears",
                  "certificates","certificatetotalscore"
                  )
    def get_certificatetotalscore(self,obj):
        certificateinfo = IndexUserCertificate.objects.filter(user=obj.user)
        scoret = 0
        if certificateinfo:
            for cer in certificateinfo:
                scoret = cer.certificate.score + scoret
        else:
            scoret = 0
        if obj.cscore != scoret:
            obj.cscore = scoret
            obj.save()
        else :
            scoret =obj.cscore
        return scoret
    def get_certificates(self,obj):
        #all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_category_id=obj.id)|Q(category__parent_category__parent_category_id=obj.id))
        certificateinfo = IndexUserCertificate.objects.filter(user=obj.user)
        if certificateinfo:
            certificates_serializer = IndexUserCertificateSerializer(certificateinfo, many=True, context={'request': self.context['request']})
            return certificates_serializer.data
        else:
            return  "no certificates info"

    def get_demandyears(self,obj):
        departinfo = self.get_depart(obj)

        demandyearsres = 0

        if departinfo :
            post = obj.user.post
            rank13 = obj.user.rank13
            departtype = departinfo["dept_type"]
            if rank13 ==1 :
                demandyearsres = 1
            if rank13==2  :
                if departtype == 2 and post == "客户经理":
                    demandyearsres=2
                elif departtype == 2 and post != "客户经理":
                    demandyearsres=1
                elif departtype ==1 and post == "携款员":
                    demandyearsres=1
                elif departtype ==1 and post != "驾驶员":
                    demandyearsres =3



            return departtype
        else:
            return 2
    def get_education(self,obj):
        return UserProfile.EDUCATION_CHOICES[obj.user.education-1]
    def get_yearsofscore(self,obj):
        return self.get_scoreofyears(obj)+self.get_yearsofwork(obj)
    def get_scoreofyears(self,obj):
        return 5
    def get_yearsofwork(self,obj):
        if obj.user.joinedyears:
            return date.today().year-obj.user.joinedyears.year
        elif obj.user.joinedyears is None:
            return 0
        else:
            return 0
    def getsc(self,obj):
        return self.get_scoreofyears(obj)+self.get_yearsofwork(obj)
    def get_joinedyears(self,obj):
        return obj.user.joinedyears
    def get_rank13(self,obj):
        return obj.user.rank13
    def get_post(self,obj):
        return obj.user.post
    def get_depart(self,obj):
        departinfo = IndexUserDepart.objects.filter(user=obj.user)
        if departinfo:
            departinfod = departinfo[0].depart
            departinfo_serializer = DepartSerializer(departinfod, many=False, context={'request':self.context['request']})
            return departinfo_serializer.data
        else:
            return []
    def get_idcardnumber(self,obj):
        return obj.user.idcardnumber
    def get_name(self,obj):
        return obj.user.name
    def get_ra(self,obj):
        return UserProfile.TITLE_CHOICES[obj.user.title-1]
    # def get_user(self,obj):
    #     #all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_category_id=obj.id)|Q(category__parent_category__parent_category_id=obj.id))
    #     userinfo = User.objects.filter(id=obj.user.id)
    #     if userinfo:
    #         #certificateinfod = certificateinfo._result_cache[0]
    #         userinfo_serializer = UserDetailSerializer(userinfo, many=False, context={'request': self.context['request']})
    #         return userinfo_serializer.data
    #     else:
    #         return  "no certificates info"