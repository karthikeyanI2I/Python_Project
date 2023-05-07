#urls.py
from django.contrib import admin  
from django.urls import path  
from todo_list import views  
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('admin/', admin.site.urls),  
    #path('', views.index),  
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
  
    path('login/', auth_views.LoginView.as_view(template_name='todo_list/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='todo_list/logout.html'), name='logout'),
] 