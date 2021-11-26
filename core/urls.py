from django.urls import path
from core import views

urlpatterns = [
    path('event/', views.EventView.as_view()),
]