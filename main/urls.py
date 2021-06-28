from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('index/', views.index), 
    path('index1/', views.index1),
    path('login/', views.login),
    path('pwd_reset/', views.pwd_reset),
    path('account/', views.account),
    path('bookmarks/', views.bookmarks),
    path('account_notifications/', views.account_notifications),
    path('account_history/', views.account_history),
    path('account_bookmarks/', views.account_bookmarks),
    path('account_cards/', views.account_cards),
]