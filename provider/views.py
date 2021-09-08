from django.shortcuts import render
from .forms import RegistrationForm
from .models import Provider
# Create your views here.

def register(request):
    page = 'register'
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form)
            pass
            # user = Provider.objects.create_user(form)
            # user = form.save(commit=False)
            # user.username = user.username.lower()
            # user.save()
    context = {'page':page,'form':form}
    return render(request,'provider/login_register.html',context)
