from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('submit', views.submit, name='submit'),
    path('add_contact', views.add_contact, name='add_contact'),
    path(
      'delete/<int:pk>', views.DeleteComment.as_view(),name="comment_delete"),
]
