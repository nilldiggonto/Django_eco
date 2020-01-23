from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from .forms import ContactForm

# def home_page(request):
#     return HttpResponse('hlw world <h1>Hlw Duniya </h1>')

def home_page(request):
    template = 'home_page.html'
    context = {
        'title':'Home Page',
        'content':'Welcome to Home Page',
        
    }
    # user = request.user.is_authenticated

    if request.user.is_authenticated:
        # print(user)
        context['premium_user']='(VIP)'
    return render(request,template,context)

def about_page(request):
    template = 'home_page.html'
    context = {
        'title':'About Page',
        'content':'Welcome to About Page'
    }
    return render(request,template,context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    template = 'contact/contact.html'
    context = {
        'title':'Contact Page',
        'content':'Welcome to Contact Page',
        'form' : form
    }
    if form.is_valid():

        print(form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({'message':'Thank you'})

    if form.errors:
        errors = form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors,status=400,content_type='application/json')
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('messages'))
    return render(request,template,context)

