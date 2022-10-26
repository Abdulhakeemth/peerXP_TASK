from django.urls import path
from .views import DetailManageTickectlist, DetailNewDepartmentlist, ListUser,ListDepartment, ManageTickectlist,NewDepartmentlist,NewTickectlist

urlpatterns =[
    path('user',ListUser.as_view(),name='user'),
    path('department',ListDepartment.as_view(),name='department'),
    path('newdepartment',NewDepartmentlist.as_view(),name='newdepartment'),
    path('newdepartment/<int:pk>/',DetailNewDepartmentlist.as_view(),name='singlenewdepartment'),
    path('newtickect',NewTickectlist.as_view(),name='newtickect'),
    path('managetickect',ManageTickectlist.as_view(),name='managetickect'),
    path('managetickect',DetailManageTickectlist.as_view(),name='managetickect')
    
]