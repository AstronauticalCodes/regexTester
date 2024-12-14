from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('/result/<int:pk>/', views.ResultView.as_view(), name='result'),
]