from django.urls import path

from .views import PostList, PostDetail, PostListNews, PostDetailNews

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('news/', PostListNews.as_view()),
   path('news/<int:pk>/', PostDetailNews.as_view()),
]