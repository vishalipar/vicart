from django.contrib import auth, messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# <<<<<<< HEAD


# from cart.models import Cart
# =======
from cart.models import Cart
# >>>>>>> caf6102fd222ff60697431bf4ce4180c679b7ff9

from .forms import RegistrationForm
from .models import Account

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
            
            # USER ACTIVATION email sending
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/acount_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            # business login
            if user.type == 'business':
                return redirect('/accounts/login/business_login/?command=verification&email=',+email)
            
            return redirect('/accounts/login/?command=verification&email='+email)
        else:
            print('form is invalid',form.errors)
        
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html', context)
    
    
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated.")
        
        return redirect('login')
        
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')
            
    
def login(request):   
    if request.method == 'POST': 
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        # print(password, email, user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    
    return render(request, 'accounts/login.html')
    
# <<<<<<< HEAD
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,"You are logged out.")
    return redirect('login')

    
# =======
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
    
    
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact = email)
            
            # FORGOT PASSWORD EMAIL SEND
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Password Reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')
    
def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'Please reset your password.')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')
        
        
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successfully')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
       
    else:     
        return render(request, 'accounts/resetPassword.html')
    
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
    
    
# business 
# >>>>>>> caf6102fd222ff60697431bf4ce4180c679b7ff9
def business_login(request):
    return render(request, 'accounts/business/business_login.html')