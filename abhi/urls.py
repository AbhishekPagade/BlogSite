from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('blogs',views.blogs , name='blogs'),
    path('addblog/', views.add_blog , name= 'addblog'),
    path('addblog/add_blogs_handler',views.add_blogs_handler , name='abp'),
    path('addblog/delete_blogs_handler',views.delete_blogs_handler, name='delete'),
    path('testform', views.test, name='test-form'),
    path('testing', views.submit , name='submit'),
    path('model_form',views.modelsForm , name='model_form'),
    path('delete/<id>',views.delete_by_id,name='delete_by_id'),
    path('update/<id>',views.update_blog,name='update_blog'),
    path('update_data/<id>',views.update_data, name='update_data')


]



