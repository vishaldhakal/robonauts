from django.shortcuts import render
from .models import blog
from django.core.paginator import Paginator

def blogs_list(request):
    blogss = blog.objects.all()
    paginator = Paginator(blogss, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'blogs':page_obj,
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
