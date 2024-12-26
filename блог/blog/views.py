from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from  blog.models import Post
 
 
def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
 
    context = {
        "postList": postList,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/home.html", context)
 
def single(request, id=None):
    return render(request, "partial/single.html")

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
 Названеи статьи = request.POST['tietle']
Описание = request.POST['descript']
Ключевые слова = request.POST['keywords']
Изображение =request.POST['image']
Содержание = request.POST['content']
 member =  POST(tietlename=Названеи статьи, descriptname=Ключевые слова,keywordsname=Ключевые слова,imagename=Изображение,contentname=Содержание)
  member.save()
  return HttpResponseRedirect(reverse('index'))
