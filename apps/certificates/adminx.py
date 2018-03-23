

import xadmin
from xadmin import views
from .models import Cerficates, IndexUserCertificate

class CertificatesAdmin(object):
    list_display = ["name", "desc", "score","add_time"]

class IndexUserCertificateAdmin(object):
    list_display = [ "user","certificate","image","add_time","update_time"]

xadmin.site.register(Cerficates, CertificatesAdmin)
xadmin.site.register(IndexUserCertificate, IndexUserCertificateAdmin)