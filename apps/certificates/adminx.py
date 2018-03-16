

import xadmin
from xadmin import views
from .models import Cerficates

class CertificatesAdmin(object):
    list_display = ["user","name", "desc", "score","add_time"]




xadmin.site.register(Cerficates, CertificatesAdmin)