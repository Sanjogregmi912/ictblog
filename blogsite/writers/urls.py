from django.urls import path
from writers import views

urlpatterns = [
    path('login', views.login),
    path('addstaff', views.addstaff),
    path('viewstaff', views.viewstaff),
    path('dashboard',views.dashboard)
]
