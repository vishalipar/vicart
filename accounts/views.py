from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from .models import Account
from django.shortcuts import redirect
# Create your views here.

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)        
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            type = form.cleaned_data['type']
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,type=type,username=username)
            user.phone_number = phone_number
            user.save()
            
            
            
            return redirect('/accounts/login/?command=verification&email='+email)
        else:
            print('form is invalid',form.errors)
        
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html', context)
    
def login(request):
    return render(request, 'accounts/login.html')
    
def business_login(request):
    return render(request, 'accounts/business/business_login.html')