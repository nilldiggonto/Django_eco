from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from .forms import LoginForm,RegisterForm,GuestForm
from .models import GuestEmail
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, FormView

# Create your views here.


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    template= 'accounts/auth/login.html'
    context = {
        'form':form

    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email   = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        
        if is_safe_url(redirect_path, request.get_host()):

            return redirect(redirect_path)
        else:
            return redirect('/register')                                  #context['form']= LoginForm()
                                                     #print(form.cleaned_data)

    return redirect('/register/')


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/auth/login.html'
    def form_valid(self,form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=email,password=password)    #print(request.user.is_authenticated)
        if user is not None:     
            
            try:
                del request.session['guest_email_id']
            except:
                pass#print(user)
            
            login(request,user)
            if is_safe_url(redirect_path, request.get_host()):

                return redirect(redirect_path)
            else:
                return redirect('/')   
        return super(LoginView,self).form_invalid(form)
        


# def login_page(request):
#     form = LoginForm(request.POST or None)
#     template= 'accounts/auth/login.html'
#     context = {
#         'form':form

#     }
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(request,username=username,password=password)    #print(request.user.is_authenticated)
#         if user is not None:     
            
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass#print(user)
            
#             login(request,user)
#             if is_safe_url(redirect_path, request.get_host()):

#                 return redirect(redirect_path)
#             else:
#                 return redirect('/')                                  #context['form']= LoginForm()
#         else:
#             print('Fixed me later')                                                #print(form.cleaned_data)

#     return render(request,template,context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/auth/register.html'
    success_url = '/login/'

# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     template= 'accounts/auth/register.html'
#     context = {
#         'form':form,
#     }
#     if form.is_valid():
#         form.save()
#         # username = request.POST.get('username')
#         # email    = request.POST.get('email')
#         # password = request.POST.get('password')
#         # new_user = User.objects.create_user(username,email,password)
#         # return redirect('/login')
    
#     return render(request,template,context)