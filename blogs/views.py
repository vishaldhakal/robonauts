from django.shortcuts import render
from .models import blog

def blogs_list(request):
    blogss = blog.objects.all()
    context = {
        'blogs':blogss,
    }
    return render(request,'blogs_list.html',context)

def blog_single(request,slug):
    blogs = blog.objects.all()
    blogss = blog.objects.get(slug=slug)
    context = {
        'blog':blogss,
        'blogs':blogs,
    }
    return render(request,'blog_single.html',context)
