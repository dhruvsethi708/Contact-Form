from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    return render(request, 'home.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return redirect('dashboard')
    return render(request, 'contact_form.html')

def dashboard(request):
    contacts = Contact.objects.all()
    return render(request, 'dashboard.html', {'contacts': contacts})
