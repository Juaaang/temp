from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
            
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:detail', pk=article.pk)
    
    else:
        return render(request, 'articles/create.html')
    
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')

        article.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        context={'article':article}
        return render(request, 'articles/update.html', context)

    
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    msg1 = request.GET.get('msg1')
    msg2 = request.GET.get('msg2')
    context = {
        'msg1':msg1,
        'msg2':msg2,
    }
    return render(request, 'articles/catch.html', context)