import xadmin
from xadmin import views
from .models import DepartDetail,IndexUserDepart

class DepartAdmin(object):
    list_display = ["name", "dept_type", "parent_dept"]

class DepartUserAdmin(object):
    list_display = [ "depart","user"]

xadmin.site.register(IndexUserDepart, DepartUserAdmin)
xadmin.site.register(DepartDetail, DepartAdmin)