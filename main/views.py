from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request,'main/index.html')

def login(request):
    return render(request,'main/login.html')

# def blog(request):
#     return render(request, 'main/blog.html')
def blog(request):
    postlist  = Post.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(postlist, 5)
    postlist  = pagenator.get_page(page)
    #postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    post = {'post': Post.objects.all()}
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html',{'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                rogophoto=request.POST['rogophoto'],
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                write=request.POST['write'],
                created_date=request.POST['created_date'],
                author=request.POST['author'],
            )
        else:
            new_article=Post.objects.create(
                rogophoto=request.POST['rogophoto'],
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                write=request.POST['write'],
                created_date=request.POST['created_date'],
                author=request.POST['author'],

            )
            return HttpResponseRedirect(reverse('blog'))
    else:
        return render(request, 'main/posting.html')
        return redirect('/blog/')
    return render(request, 'main/new_post.html')
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})
