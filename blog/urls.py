from . import views
from django.urls import path

app_name= 'blog'



urlpatterns = [
    path('post/add/', views.PostCreate.as_view(), name='post-add'),
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
    path('category/', views.PostCategoryList.as_view(),  name='post_category_list'),
    path('category/<slug:slug>/', views.PostCategoryDetail.as_view(),  name='post_category'),
    path('tag/', views.PostTagList.as_view(),  name='post_tag_list'),
    path('tag/<slug:slug>/', views.PostTagDetail.as_view(),  name='post_tag'),
]