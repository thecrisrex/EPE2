from django.urls import path
from .views.viewTest import TestView

urlpatterns = [
    path('test/', TestView.as_view(), name='test-endpoint'),
  
]
