from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='board'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # 게시글 세부사항 페이지
    path('post/write/', views.post_create, name='post_create'),
]
