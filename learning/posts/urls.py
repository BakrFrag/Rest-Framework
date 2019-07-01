from django.urls import path
from posts import views;
urlpatterns = [
  path("posts/list/",views.PostApiView.as_view(),name="post_list"),
  path("posts/<int:pk>/",views.PostRetriveApiView.as_view(),name="post_detail"),
  path("posts/create/",views.PostCreateApiView.as_view(),name="post_create"),
  path("posts/update/<pk>/",views.PostUpdateApiView.as_view(),name="post_update"),
  path("posts/destorey/<pk>/",views.PostDestoryApiView.as_view(),name="post_destorey"),
  path("posts/mixins/",views.ApiWithMixins.as_view(),name="posts_mixins")
]
