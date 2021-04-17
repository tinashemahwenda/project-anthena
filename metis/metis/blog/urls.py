from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_details'),
    path('',BlogListView.as_view(),name='home'),

]

