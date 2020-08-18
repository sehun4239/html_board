from django.urls import path
from . import views
# http://localhost:8000 요청이 들어왔을때 우리 전체 project의 홈페이지로 이동시킬거다.
# Django는 elegant URL을 지원한다.
# 정규표현식(regular expression) - regex
# 시작 => ^ 끝 => $
# [] : 1글자를 지칭 , e.g. [0-9] 면 0~9까지 중에 한개를 지칭함
# {3,5} : 3번~5번 반복함   e.g. [0-9]{4} -> 4자리 숫자
# r(raw)은 escape 문자를 한번 더 사용하지 않도록 처리. -> escape문자인 \\를 \만 써도 됨
# e.g. r"^[0-9]{1,3}$" -> 한자리거나 두자리거나 세자리
# r"^010[1-9]\d{6,7}$" => 핸드폰 번호

app_name = 'posts'

urlpatterns = [
    path('list/', views.p_list, name='list'),
    path('create/', views.p_create, name='create'),
    path('<int:post_id>/', views.p_detail, name='detail'),
    path('<int:post_id>/delete/', views.p_delete, name='delete'),
    path('cannotdelete', views.n_delete, name='notdelete'),
    path('<int:post_id>/update/', views.p_update, name='update'),
    path('<int:post_id>/reply/', views.p_reply, name='reply'),
    path('<int:post_id>/like/', views.p_like, name='like'),
    path('<int:post_id>/unlike/', views.p_unlike, name='unlike'),
    path('<int:post_id>/reply/<int:reply_id>/delete/', views.r_delete, name='rdelete'),
    path('<int:post_id>/reply/<int:reply_id>/update/', views.r_update, name='rupdate'),
]
