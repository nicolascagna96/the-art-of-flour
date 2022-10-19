from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]