from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserCreate.as_view()),
    path('<slug:username>/', views.UserDetail.as_view()),
    path('follow/<int:user_id>/', views.ProfileFollow.as_view()),
    # path('<slug:username>/following/', views.UserDetail.as_view()),
    # path('<slug:username>/followers/', views.UserDetail.as_view())
]
