from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get/', views.get_cookie, name='get_cookie'),
    # path('set/', views.set_cookie, name='set_cookie'),
    path('delete/', views.delete_cookie, name='delete_cookie'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
]
