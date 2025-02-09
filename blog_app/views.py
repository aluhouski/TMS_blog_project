from django.shortcuts import render, get_object_or_404
from .models import Post

# Список всех постов
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Получаем все посты
    return render(request, 'blog_app/post_list.html', {'posts': posts})

# Просмотр отдельного поста
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_app/post_detail.html', {'post': post})