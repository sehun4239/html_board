from django.db import models
from users.models import User

class Post(models.Model):
    author = models.CharField('작성자', max_length=20)
    contents = models.CharField('글제목', max_length=100)
    texts = models.TextField('글내용', max_length=1000)
    pdate = models.DateTimeField('작성일', auto_now_add= True)
    like = models.IntegerField('추천', default=0)
    unlike = models.IntegerField('비추', default=0)

    def __str__(self):
        return self.contents

class Reply(models.Model):
    reple = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.CharField('작성자', max_length=20)
    reply = models.CharField('댓글', max_length=200)
    pdate = models.DateTimeField('작성일', auto_now= True)

    def __str__(self):
        return self.reply