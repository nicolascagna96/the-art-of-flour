from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
    #  path(
    #     'about',
    #     views.generic.TemplateView.as_view(template_name='about.html'),
    #     name='about'),
