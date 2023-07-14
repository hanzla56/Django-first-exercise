from django.contrib import admin
from django.urls import path 
from firstapp import views #Added manually

app_name = "firstapp"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index , name='index'),
    path("details/" , views.details , name='details')
]
