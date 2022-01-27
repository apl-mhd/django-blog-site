from argparse import _VersionAction
from unicodedata import name
from django.urls import path
from base import views

urlpatterns = [

    path('', views.index, name="index"),
    path('post-create', views.postCreate, name='post-create'),
    path('post-update/<int:id>/', views.postUpdate, name='post-update'),
    path('post-delete/<int:id>/', views.postDelete, name='post-delete'),
    path('post-delete-success/<int:id>/', views.postDeleteSuccess, name='post-delete-success'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register')
]
