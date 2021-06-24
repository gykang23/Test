from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum
from django.shortcuts import render
from django.views.generic import ListView



def search(request):
    posts = Post.objects.filter().order_by('-id')
    tags = request.POST.getlist('tags',None)


    # q = request.POST.get('q','')



    q = Q()
    if tags:
        q.add (Q(jop__in=tags),Q.AND)
        posts = posts.filter(jop__in=tags)
    #     posts = posts.filter(Q(jop__icontains=tags))
    return render(request, 'main/search.html', {'posts' : posts, 'tags' : tags})
    # if jop:
    #     posts = posts.filter(Q(jop__icontains=tags)&Q(jop__icontains=tags))
    #     return render(request, 'main/search.html', {'posts' : posts, 'jop' : jop})
# else :
#         return render(request, 'main/search.html')


def tags(request):
    jop = request.POST.get('',None)
    jop_count  = Post.objects.filter(jop=IT).aggregate(sum('jop'))
    pots.stories_filed += 1
    posts.save()

    return render(request, 'main/blog.html',{'jop_count': jop_count})




def index(request):
    return render(request,'main/index.html')

def login(request):
    return render(request,'main/login.html')

# def blog(request):
#     return render(request, 'main/blog.html')
def blog(request):
    postlist  = Post.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(postlist, 10)
    postlist  = pagenator.get_page(page)
    #postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

    postlist  = Post.objects.all().order_by('-id')

    search_key = request.GET.get('search_key')
    if search_key: # 만약 검색어가 존재하면
        post_list = post_list.filter(wtite__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기

    return render(request, 'main/blog.html', {'blog':blog})

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
                jop=request.POST['jop'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                write=request.POST['write'],
                # created_date=request.POST['created_date'],
                author=request.POST['author'],
            )
        else:
            new_article=Post.objects.create(
                rogophoto=request.POST['rogophoto'],
                postname=request.POST['postname'],
                jop=request.POST['jop'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                write=request.POST['write'],
                # created_date=request.POST['created_date'],
                author=request.POST['author'],

            )
        return HttpResponseRedirect(reverse('blog'))
    else:
        return render(request, 'main/new_post.html')
        return redirect('/blog/')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})
