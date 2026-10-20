from django.shortcuts import render, redirect
from django.template import Context

from .form import ContactForm

# Create your views here.
def index(request:str):
    return render(request, "asiatouragency/index.html")

def home_view(request:str):
    return render(request, "asiatouragency/home.html")

#To handle contact form
def contact_view(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("contact_success")
        else:
            form = ContactForm()

        context = {"form": form}
    return render(request, 'asiatouragency/contact.html', context)

#To handle success page
def contact_success_view(request):
    return render(request, 'asiatouragency/contact_success.html', {})
