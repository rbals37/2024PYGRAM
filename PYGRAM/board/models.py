from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # 게시글 제목
    content = models.TextField()  # 게시글 내용
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 커스텀 사용자 모델을 참조
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일자

    def __str__(self):
        return self.title  # 게시글 제목을 출력