from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<str:pk>', views.post, name="post"),
    path('form', views.form_, name="form_"),
    path('delete_post/<str:pk>', views.delete_post, name="delete_post"),
    path('update_post/<str:pk>', views.update_post, name="update_post")
]