from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog, name='blogs'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
