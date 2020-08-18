from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Reply
from .forms import PostForm, ReplyForm

def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    return render(request, 'list.html', {'posts' : my_list})

def p_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    reply_form = ReplyForm()

    if request.session.get('user_id'):
        return render(request, 'detail.html', {'post': post, 'reply_form':reply_form})
    else:
        return redirect('users:login')

def p_create(request):
    # POST 방식으로 호출될 때 / form action으로 요청하는 거 아니면 싹다 GET방식
    post = Post(author=request.session['user_id'])

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    # GET 방식으로 호출될 때
    else:
        post_form = PostForm()

    return render(request, 'create.html', {'post_form':post_form})

def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.session['user_id'] == post.author:
        post.delete()
    else:
        return redirect('posts:notdelete')
    return redirect('posts:list')

def n_delete(request):
    return render(request, 'notdelete.html')

def p_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)      # id=post_id도 가능
    # POST 방식으로 호출될 때 / form action으로 요청하는 거 아니면 싹다 GET방식
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)           #instance=post는 일종의 key값으로 이해

        if post_form.is_valid():
            post_form.save()                    # save는 key가 없으면 무조건 생성, 근데 위에 instance=post key를 줘서 대체
            return redirect('posts:list')

    # GET 방식으로 호출될 때
    else:
        if request.session['user_id'] == post.author:
            post_form = PostForm(instance=post)
        else:
            return redirect('posts:notdelete')
    return render(request, 'create.html', {'post_form':post_form})

def p_reply(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    reply = Reply(reple=post, writer=request.session['user_id'])
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST, instance=reply)

        if reply_form.is_valid():
            reply_form.save()
    return redirect('posts:detail', post_id)

def p_like(requeset, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.like += 1
    post.save()
    return redirect('posts:detail', post_id)

def p_unlike(requeset, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.unlike += 1
    post.save()
    return redirect('posts:detail', post_id)

def r_delete(request, post_id, reply_id):
    replyreal = Reply.objects.get(id=reply_id)
    if request.session['user_id'] == replyreal.writer:
        replyreal.delete()
    else:
        return redirect('posts:notdelete')
    return redirect('posts:detail', post_id)

def r_update(request, post_id, reply_id):
    reply = Reply.objects.get(id=reply_id)

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST, instance=reply)           #instance=post는 일종의 key값으로 이해

        if reply_form.is_valid():
            reply_form.save()                    # save는 key가 없으면 무조건 생성, 근데 위에 instance=post key를 줘서 대체
            return redirect('posts:detail', post_id)

    # GET 방식으로 호출될 때
    else:
        if request.session['user_id'] == reply.writer:
            reply_form = ReplyForm(instance=reply)
        else:
            return redirect('posts:notdelete')

    return render(request, 'rupdate.html', {'reply_form':reply_form})