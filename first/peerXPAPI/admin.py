from django.contrib import admin
from .models import ManageTicket, NewTickect, User,Department,NewDepartment
admin.site.register(Department)
admin.site.register(User)
admin.site.register(NewDepartment)
admin.site.register(NewTickect)
admin.site.register(ManageTicket)