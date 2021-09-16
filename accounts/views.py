from accounts.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm

# Create your views here.
def registerAccount(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'page':'register', 'form':form}
    return render(request, 'accounts/login_register.html',context)

def loginAccount(request):
    context = {'page':'login'}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user= User.objects.get(email=email)
        except:
            print('username does not exist')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('bus.dashboard')
        else:
            print('username or password incorrect')
    return render(request,'accounts/login_register.html',context)

def dashboard(request):
    pass

def staff():
    pass