from django.shortcuts import render, get_object_or_404
from blog.models import Article


def index(request):
    data = Article.objects.all()

    context = {
        "data": data,
    }

    return render(request, "list.html", context)

def detail(request, post_id):
    post = get_object_or_404(Article, id=post_id)

    context = {
        "post": post,
    }

    return render(request, "detail.html", context)
