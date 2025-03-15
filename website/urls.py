from django.urls import path, include 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.customer_record, name = 'cutomer_record'),
    path('record/delete/<int:pk>', views.delete, name='delete'),
    path('create_record/', views.create_record, name ='create_record'),
    path('update_record/<int:pk>', views.update_record, name='update'),
    path('search/', views.search, name='search')
]
