from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='password' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='password Confirmation', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields =['email',]


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 != password2:
            raise forms.ValidationError('Password dont match')
        return password2

    def save(self,commit=True):
        user = super(UserAdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            users.save()
        return user

class UserAdminChangedForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password','active','admin')

    def clean_password(self):
        return self.initial['password']











class GuestForm(forms.Form):
    email    = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control','id':'form-control','placeholder':'Email@gmail.com'}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'form-control','id':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'form-control','placeholder':'Type Password'}))














class RegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(label='password' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='password Confirmation', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields =['full_name', 'email',]


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 != password2:
            raise forms.ValidationError('Password dont match')
        return password2

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        # user.active = False
        if commit:
            user.save()
        return user















# class RegisterForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'form-control','placeholder':'username'}))
#     email    = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','id':'form-control','placeholder':'Email@gmail.com'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'form-control','placeholder':'Type Password'}))
#     password2= forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'form-control','placeholder':'Confirm Password'}))

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError('Username already Exists')
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError('Email already Exists')
#         return email

#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2= self.cleaned_data.get('password2')

#         if password2 != password:
#             raise forms.ValidationError('Password do not match!!')
#         return data