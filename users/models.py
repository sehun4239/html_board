from django.db import models

class User(models.Model):
    username = models.CharField('이름', max_length=12)
    password = models.CharField('비밀번호', max_length=24)
    useremail = models.EmailField('이메일', max_length=72)
    registered_date = models.DateTimeField('가입일', auto_now_add=True)

    def __str__(self):
        return self.username