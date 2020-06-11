from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="articles_list_url"),
    path('article/create/', ArticleCreate.as_view(), name="article_create_url"),
    path('article/<str:slug>/update', ArticleUpdate.as_view(), name="article_update_url"),
    path('article/<str:slug>/delete/', ArticleDelete.as_view(), name="article_delete_url"),
    path('article/<str:slug>/', ArticleDetail.as_view(), name="article_detail_url"),
    # comments
    path('article/<str:slug>/comment/create/', ArticleCommentCreate.as_view(), name="article_comment_create_url"),
    path('article/<str:slug>/comment/<str:comment_slug>/update', ArticleCommentUpdate.as_view(), name="article_comment_update_url"),
    path('article/<str:slug>/comment/<str:comment_slug>/delete', ArticleCommentDelete.as_view(), name="article_comment_delete_url"),
]
