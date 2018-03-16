from django.db import models
from datetime import datetime

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class CoefficientDetail(models.Model):
    """
    系数明细
    """
    user = models.OneToOneField(User, verbose_name=u"用户")
    yscore = models.IntegerField(default=0,verbose_name="年限得分",help_text="年限得分")
    escore = models.IntegerField(default=0,verbose_name="学历得分",help_text="学历得分")
    tscore =models.IntegerField(default=0,verbose_name="职称得分",help_text="职称得分")
    pccbpscore =models.IntegerField(default=0,verbose_name="银行从业得分",help_text="银行从业得分")
    iccbpscore =models.IntegerField(default=0,verbose_name="中级银行从业得分",help_text="中级银行从业得分")
    itscore =models.IntegerField(default=0,verbose_name="内训师得分",help_text="内训师得分")
    cscore =models.IntegerField(default=0,verbose_name="其他证书得分",help_text="其他证书得分")
    totalscore =models.IntegerField(default=0,verbose_name="总得分",help_text="总得分")
    rank =models.IntegerField(default=0,verbose_name="级次",help_text="级次")
    coefficent = models.FloatField(default=0,verbose_name="系数",help_text="系数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")

    class Meta:
        verbose_name = "员工系数"
        verbose_name_plural = verbose_name
        unique_together = ("user", "coefficent")

    def __str__(self):
        return self.user.name+" "+self.rank+" " +self.coefficent