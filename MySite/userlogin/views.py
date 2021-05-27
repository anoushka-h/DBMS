from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from userlogin.forms import SignUpForm

# Create your views here.
def signup(request):
    #if request.user.is_authenticated:
        #return redirect('login')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            return redirect('login')
        else:
            return render(request, 'userlogin/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'userlogin/signup.html', {'form': form})

