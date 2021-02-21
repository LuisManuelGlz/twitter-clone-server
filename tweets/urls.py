from django.urls import path
from . import views

urlpatterns = [
    path('', views.TweetList.as_view()),
    path('<int:pk>/', views.TweetDetail.as_view()),
    path('<int:pk>/like/', views.TweetLike.as_view()),
    path('<int:pk>/likes/', views.LikesDetail.as_view()),
]
