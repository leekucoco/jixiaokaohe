# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from datetime import datetime,date

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()
from rank13.models import Rank13Coefficent,Rank13Demands
from certificates.models import IndexUserCertificate

class CoefficientDetail(models.Model):
    """
    系数明细
    """
    user = models.OneToOneField(User, verbose_name=u"用户")
    rank13demands = models.ForeignKey(Rank13Demands,  verbose_name=u"岗位等级及岗位要求", default=1)
    rank13coefficent = models.ForeignKey(Rank13Coefficent, verbose_name=u"系数", default=1)
    # yscore = models.IntegerField(default=0,verbose_name="年限得分",help_text="年限得分")
    # escore = models.IntegerField(default=0,verbose_name="学历得分",help_text="学历得分")
    # tscore =models.IntegerField(default=0,verbose_name="职称得分",help_text="职称得分")
    # pccbpscore =models.IntegerField(default=0,verbose_name="银行从业得分",help_text="银行从业得分")
    # iccbpscore =models.IntegerField(default=0,verbose_name="中级银行从业得分",help_text="中级银行从业得分")
    # itscore =models.IntegerField(default=0,verbose_name="内训师得分",help_text="内训师得分")
    # cscore =models.IntegerField(default=0,verbose_name="其他证书得分",help_text="其他证书得分")
    # totalscore =models.IntegerField(default=0,verbose_name="总得分",help_text="总得分")
    # rank =models.IntegerField(default=0,verbose_name="级次",help_text="级次")
    # coefficent = models.FloatField(default=0,verbose_name="系数",help_text="系数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")
    is_special = models.BooleanField(default=False,verbose_name="是否为特殊指定系数")

    class Meta:
        verbose_name = "员工系数"
        verbose_name_plural = verbose_name
        unique_together = ("user", "rank13coefficent")

    def __str__(self):
        return self.user.username
    def get_yearsofwork(self):#获取工作年限
        if self.user.joinedyears:
            return date.today().year-self.user.joinedyears.year
        elif self.user.joinedyears is None:
            return 0
        else:
            return 0
    def get_demandyears(self):#获取要求工作年限
        return self.rank13demands.demandyears
    def get_scoreofyears(self):#获取年限得分
        demands = self.get_demandyears()
        yearsofwork = self.get_yearsofwork()
        if yearsofwork == demands:
            return 0
        elif yearsofwork > demands:
            return round((yearsofwork-demands)/2)*1
        elif yearsofwork < demands:
            return (yearsofwork-demands)*2
    def get_education(self):#获取学历
        return self.user.education
    def get_demandeducation(self):#学历要求
        return self.rank13demands.educationdemands
    def get_scoreofeducation(self):#学历得分
        education = self.get_education()
        demandeducation = self.get_demandeducation()
        return education-demandeducation
    def get_title(self):#职称
        return self.user.title
    def get_demandtitle(self):#职称要求
        return self.rank13demands.titledemands
    def get_scoreoftitle(self):#职称得分
        title =self.get_title()
        demandtitle = self.get_demandtitle()
        return title - demandtitle
    def get_primccbp(self):#初级银行从业
        return self.user.primccbp
    def get_demandprimccbp(self):#初级银行从业要求
        return self.rank13demands.primccbpdemands
    def get_scoreofprimccbp(self):#初级银行从业得分
        primccbp = self.get_primccbp()
        demandprimccbp = self.get_demandprimccbp()
        return primccbp-demandprimccbp
    def get_intermediateccbp(self):#中级银行从业
        return self.user.intermediateccbp
    def get_scoreofintermediateccbp(self):
        return self.get_intermediateccbp()*2
    def get_internel_trainer(self):#内训师
        return self.user.internel_trainer
    def get_scoreofinternel_trainer(self):
        return self.get_internel_trainer()-1

    def get_certificatetotalscore(self):
        certificateinfo = IndexUserCertificate.objects.filter(user=self.user)
        scoret = 0
        if certificateinfo:
            for cer in certificateinfo:
                scoret = cer.certificate.score + scoret

        else:
            scoret = 0
        return scoret

    def get_total_score(self):
        rank = self.rank13demands.rank
        totalscore = 0
        scoreofyears = self.get_scoreofyears()
        scoreofeducation = self.get_scoreofeducation()
        scoreoftitle = self.get_scoreoftitle()
        scoreofprimccbp = self.get_scoreofprimccbp()
        scoreofintermediateccbp = self.get_scoreofintermediateccbp()
        scoreofinternel_trainer = self.get_scoreofinternel_trainer()
        certificatetotalscore = self.get_certificatetotalscore()
        totalscore = (scoreofyears+scoreofeducation+scoreofprimccbp+scoreoftitle+
                      scoreofintermediateccbp+scoreofinternel_trainer+
                      certificatetotalscore)

        return totalscore
    def get_level(self):#级次
        totalscore = self.get_total_score()
        level = 1
        if totalscore <= -10:
            level = 1
        elif -10< totalscore <= -5:
            level = 2
        elif -5 <totalscore <5:
            level = 3
        elif 5<= totalscore< 10:
            level = 4
        elif 10 <= totalscore:
            level = 5
        else :
            level = 0
        return level

    def ensureranklevel(self):
        rank = self.rank13demands.rank
        level = self.get_level()
        if self.is_special == False:
            co = Rank13Coefficent.objects.get(level=level, rank=rank)
            if self.rank13coefficent != co:
                self.rank13coefficent = co
                self.save()
                return  self.user.username, "成功更新用户等级系数"
            else:
                return self.user.username, "等级系数匹配无需更改"
        elif self.is_special == True:
            return self.user.username, "特殊系数用户无法更改"
