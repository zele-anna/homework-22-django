from django.urls import path
from blog.apps import BlogConfig
from blog import views

app_name = BlogConfig.name

urlpatterns = [
    path('article_list/', views.ArticleListView.as_view(), name='article_list'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),

]
