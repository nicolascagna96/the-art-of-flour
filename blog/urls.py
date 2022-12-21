from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_contact', views.add_contact, name='add_contact'),
    path(
      'delete/<int:pk>', views.DeleteComment.as_view(),name="comment_delete"),
    path('submit', views.CreatePostView.as_view(), name='submit'),
    path(
        '<slug:slug>/update/',
        views.UpdatePostView.as_view(),
        name='post_update'),
    path(
        '<slug:slug>/delete/',
        views.DeletePostView.as_view(),
        name='post_delete'),
   
    path(
        '<slug:slug>/delete/',
        views.DeletePostView.as_view(),
        name='delete_post'),
]
