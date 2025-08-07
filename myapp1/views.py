from django.shortcuts import render

def homepage(request):
    return render(request, 'myapp1/homepage.html')
def contact(request):
    return render(request, 'myapp1/contact.html') 
def about(request):
    return render(request, 'myapp1/about.html') 
def resume(request):
    return render(request, 'myapp1/resume.html')
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        send_mail(
            subject='New Contact Message',
            message=full_message,
            from_email='nourhene.rhouma@yahoo.com',
            recipient_list=['nourhene.rhouma@yahoo.com'],
        )

        messages.success(request, "Your message has been sent!")

    return render(request, 'myapp1/contact.html')