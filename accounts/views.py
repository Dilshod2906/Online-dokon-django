from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, change_password
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.





# Create your views here.
def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                
                data = form.cleaned_data
                user = authenticate(request,
                    username = data['username'],
                    password = data['password']
                )
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return HttpResponse("<h2>Sizning akkauntingiz faol emas</h2>")
                else:
                    
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    

                    
        else:
            form = LoginForm()
            context = {
                'form' : form,
                
                
            }
        return render(request, 'accounts/login.html',context)
    
    else:
        return HttpResponseRedirect(reverse('profile'))

            
@login_required(login_url='/accounts/login/')
def profile(request):

    if request.method == 'POST':
        user_form = change_password(data=request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data

            u = User.objects.get(username=request.user)
            u.set_password(f"{data['passwordc']}")
            u.save()
            user = authenticate(request,
                    username = request.POST,
                    password = data['passwordc']
                )
            if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('profile'))
 

    else:
            user_form = change_password()
    context = {
        'user_form':user_form
    }
    return render(request, 'accounts/profile.html', context)



def logout1(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def UserRegisterView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserRegistrationForm(data=request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(
                    user_form.cleaned_data['password1']
                )
                new_user.save()
                Profile.objects.create(user=new_user)

                return HttpResponseRedirect(reverse('login'))
        else:
            user_form = UserRegistrationForm()
        context = {'user_form': user_form}
        return render(request, 'accounts/register.html',context)
    else:
        return HttpResponseRedirect(reverse('profile'))
