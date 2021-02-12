from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserCreate.as_view()),
    path('<slug:username>/', views.UserDetail.as_view())
]
