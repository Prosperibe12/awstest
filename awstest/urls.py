from django.urls import path 
from . import views

urlpatterns = [
  path('health/', views.APIHealthCheck.as_view(), name='health-check')
]
