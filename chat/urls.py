from django.urls import path
from chat.views.viewDeepseek import DeepSeekView

urlpatterns = [
    path('deepseek/', DeepSeekView.as_view(), name='deepseek'),
]
