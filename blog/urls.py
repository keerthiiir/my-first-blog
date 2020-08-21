from django.urls import path
from . import views

urlpatterns = [
#path('',views.main_page, name='main_page'),
path('', views.post_list, name='post_list'),
path('post/<int:pk>/', views.post_detail, name='post_detail'),
path('post/new/', views.post_new, name='post_new'),
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
path('CV/', views.CVpost_list, name='CVpost_list'),
path('CV/new/',views.CVpost_new, name='CVpost_new'),
path('CV/<int:pk>/edit/', views.CVpost_edit, name='CVpost_edit')
]