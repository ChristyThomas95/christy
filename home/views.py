from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'home.html')


def skills(request):
    return render(request, 'pages/skills.html')

def projects(request):
    return render(request, 'pages/projects.html')


def projectdetails(request):
    return render(request, 'pages/projectdetails.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
       
        
        email_subject = 'You have a new email from your  site' + subject
        message_body = 'Name: ' + name + '\nEmail: ' + email + 'Message:' + message
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        
        send_mail(
            email_subject,
            message_body,
            'kristythomas.95@gmail.com',
            [admin_email],
            fail_silently=False,   
        )
        messages.success(request, 'Thanks for contacting me, I will get back to you soon')
        return redirect('home')
        
    return render(request, 'pages/contact.html')