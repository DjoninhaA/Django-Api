from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.get_all_users, name='all_users'),
    path('user/<int:id>', views.get_by_id, name='get_user'),
    path('user/create',views.create_user, name='create_user'),
    path('user/update/<int:id>',views.update_user, name='update_user'),
]