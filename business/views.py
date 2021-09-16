from django.db.models.expressions import F
from business.forms import BusinessProfileForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def dashboard(request):
    context = {'page_title':'Business Dashboard'}
    return render(request,'business/dashboard.html',context);

@login_required(login_url = "login")
def profile(request):
    form = BusinessProfileForm()
    if request.user.is_authenticated:
        user = request.user.id
        if request.method == 'POST':
            form = BusinessProfileForm(request.POST)
            if form.is_valid:
                form = form.save(commit=False)
                print(user)
                form.user_id = user
                form.save()
                messages.success(request,'business profile added successfully')
                return redirect('bus.profile')
    context = {'page_title':'Business Profile','form':form}
    return render(request,'business/profile.html',context);

def services(request):
    context = {'page_title':'Business Services'}
    return render(request,'business/services.html',context);