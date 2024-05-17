from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from django.shortcuts import redirect

app_name = 'core'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>',views.details,name='details'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LoginForm), name='login'),
    path('delete/<int:pk>',views.delete_task,name='delete'),
    path('edit/<int:pk>',views.edit_task,name='edit'),
    path('add/',views.add_task,name='add'),
    path('logout',views.log_out,name='logout'),
    path('signup/',views.sign_up,name='signup')
    
]
