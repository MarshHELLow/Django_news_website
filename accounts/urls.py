from django.urls import path
from . import views

app_name = 'accounts'  # Пространство имен

urlpatterns = [
    path('', views.account_view, name='accounts'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]