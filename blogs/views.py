from django.shortcuts import render

def blogs_list(request):
    return render(request,'blogs_list.html')
