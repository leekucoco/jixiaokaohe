from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    EDUCATION_CHOICES = (
        (1, "中专、高中及以下"),
        (2, "专科"),
        (3, "本科"),
        (4, "硕士研究生"),
        (5, "博士"),
        (6, "教授"),
    )
    TITLE_CHOICES = (
        (1, "无"),
        (2, "初级"),
        (3, "中级"),
        (4, "高级"),
    )
    INTERNEL_TRAINER_CHOICES = (
        (1, "无"),
        (2, "初级"),
        (3, "中级"),
        (4, "高级"),
    )
    CLERKRANK_CHONCES=(
        (1, "无"),
        (2, "见习柜员"),
        (3, "初级柜员"),
        (4, "中级柜员"),
        (5, "高级柜员"),
        (6, "资深柜员"),

    )
    CMANAGERLEVEL_CHOICES=(
        (1, "无"),
        (2, "一等"),
        (3, "二等"),
        (4, "三等"),
    )
    CMANAGERRANK_CHOICES=(
        (1, "无"),
        (2, "初级"),
        (3, "中级"),
        (4, "高级"),
    )

    idcardnumber = models.CharField(max_length=18, null=True, blank=True, verbose_name="身份证号")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    # depart = models.ForeignKey("DepartDetail", verbose_name="机构", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")),
                              default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    joinedyears = models.DateField(null=True, blank=True, verbose_name="参加工作年月")
    education = models.IntegerField(default=1, choices=EDUCATION_CHOICES, verbose_name="学历",
                                      help_text=u"学历: 1(本科),2(中专、高中及以下),3(专科),4(硕士研究生),5(博士),6(教授)")
    title = models.IntegerField(default=1, choices=TITLE_CHOICES, verbose_name="职称",
                                help_text=u"职称: 1(无),2(初级),3(中级),4(高级)")
    internel_trainer = models.IntegerField(default=1,choices=INTERNEL_TRAINER_CHOICES,verbose_name="内训师",
                                           help_text=u"内训师: 1(无),2(初级),3(中级),4(高级)")
    yscore = models.IntegerField(default=0,verbose_name="年限得分",help_text="年限得分")
    cmanagerlevel = models.IntegerField(default=1,choices=CMANAGERLEVEL_CHOICES,verbose_name="客户经理等次",
                                           help_text=u"客户经理等次: 1(无),2(一等),3(二等),4(三等)")
    cmanagerrank = models.IntegerField(default=1,choices=CMANAGERRANK_CHOICES,verbose_name="客户经理级次",
                                           help_text=u"客户经理级次: 1(无),2(初级),3(中级),4(高级)")

    clerkrank = models.IntegerField(default=1,choices=CLERKRANK_CHONCES,verbose_name="柜员等级",
                                           help_text=u"柜员等级: 1(无),2(见习),3(初级),4(中级),5(高级),6(资深)")
    rank13 = models.IntegerField(default=1, verbose_name="行员等级", help_text="行员等级(共13等)")
    primccbp = models.IntegerField(default=0, verbose_name="初级银行从业", help_text="初级银行从业")
    intermediateccbp = models.IntegerField(default=0, verbose_name="中级银行从业", help_text="中级银行从业")
    post = models.CharField(null=True, blank=True, max_length=11, verbose_name="岗位")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# class VerifyCode(models.Model):
#     """
#     短信验证码
#     """
#     code = models.CharField(max_length=10, verbose_name="验证码")
#     mobile = models.CharField(max_length=11, verbose_name="电话")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name = "短信验证码"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.code



