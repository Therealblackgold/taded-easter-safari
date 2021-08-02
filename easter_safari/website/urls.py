from django.urls import path
from . import views
from .views import PostView

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
]
