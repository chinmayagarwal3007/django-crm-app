from django.urls import path, include 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name = 'cutomer_record'),
    path('record/delete/<int:pk>', views.delete, name='delete'),
]
