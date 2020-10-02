from django.shortcuts import render,redirect
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def games(request):
    return render(request,'games.html')

def contact(request):
    return render(request,'contact.html')

def send_mails(request):
    if request.method == "POST":
        subject = "Contact"
        fromm = request.POST['from']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        send_mail(
        subject,
        message,
        email,
        ['teamrobonauts.np@gmail.com','vishaldhakal96@gmail.com']
        )
        if fromm == "index_page":
            return redirect('index')
        else:
            return redirect('contact')

    return render(request,'index.html')