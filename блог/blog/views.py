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
tietle= request.POST['tietle']
descript = request.POST['descript']
keywords = request.POST['keywords']
image =request.POST['image']
content = request.POST['content']
 member =  Post (title=tietle, description=descript, keywords =keywords, image=image, content=content)
  member.save()
  return HttpResponseRedirect(reverse('index'))
