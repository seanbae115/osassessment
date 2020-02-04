from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('<int:id>/', views.register_user, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
