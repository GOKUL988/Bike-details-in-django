from django.urls import path
from. import views
urlpatterns=[
    path("",views.home, name='home.html'),
    path("read",views.read, name='read.html'),
    path("create",views.create, name='create.html'),
    path("update",views.update, name='update.html'),
    path("updatebike/<int:id>",views.updatebike, name='updatebike.html'),
    path("delete",views.delete,name='delete.html'),
    path("deletebike/<int:id>",views.deletebike, name='deletebike.html'),
]