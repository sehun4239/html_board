"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView


# http://localhost:8000 요청이 들어왔을때 우리 전체 project의 홈페이지로 이동시킬거다.
# Django는 elegant URL을 지원한다.
# 정규표현식(regular expression) - regex
# 시작 => ^ 끝 => $
# [] : 1글자를 지칭 , e.g. [0-9] 면 0~9까지 중에 한개를 지칭함
# {3,5} : 3번~5번 반복함   e.g. [0-9]{4} -> 4자리 숫자
# r(raw)은 escape 문자를 한번 더 사용하지 않도록 처리. -> escape문자인 \\를 \만 써도 됨
# e.g. r"^[0-9]{1,3}$" -> 한자리거나 두자리거나 세자리
# r"^010[1-9]\d{6,7}$" => 핸드폰 번호

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
]
