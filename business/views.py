from django.db.models.expressions import F
from business.forms import BusinessProfileForm
from django.shortcuts import redirect, render

# Create your views here.

def dashboard(request):
    context = {'page_title':'Business Dashboard'}
    return render(request,'business/dashboard.html',context);

def profile(request):
    form = BusinessProfileForm()
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('bus.dashboard')
    context = {'page_title':'Business Profile','form':form}
    return render(request,'business/profile.html',context);

def services(request):
    context = {'page_title':'Business Services'}
    return render(request,'business/services.html',context);