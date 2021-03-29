from django.urls import path
from site1_app import views

app_name = 'site1_app'

urlpatterns = [
    path('users/', views.users, name='users'),
    path('alternate/', views.alternate, name='alternate'),
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='user_login'),
]