from business import forms
from business.models import Amenities, Business, PaymentMethods
from django.db.models.expressions import F
from business.forms import BusinessAmenitiesForm, BusinessPaymentMethodsForm, BusinessProfileForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def dashboard(request):
    context = {'page_title':'Business Dashboard'}
    return render(request,'business/dashboard.html',context);

@login_required(login_url = "login")
def profile(request):
    user = request.user.id
    bus_count =Business.objects.filter(user_id=user).count();
    bus = Business.objects.filter(user_id=user).first()
    if bus_count == 0:
        form = BusinessProfileForm()
    else:
        form = BusinessProfileForm(instance=bus)
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST)
        if form.is_valid:
            if(bus_count <1):
                form = form.save(commit=False)
                form.user_id = user
                form.save()
                messages.success(request,'business profile added successfully')
                return redirect('bus.profile')
            else:
                form = BusinessProfileForm(request.POST,instance=bus) 
                form.save()
                messages.success(request,'business profile updated successfully')
                return render(request,'business/profile.html',{'form': form})
    
    context = {'page_title':'Business Profile','form':form}
    return render(request,'business/profile.html',context);

def options(request,type='all'):
    user = request.user.id
    business = Business.objects.filter(user_id=user).first()
    amenities = Amenities.objects.filter(business_id = business)
    amenities_count = amenities.count()
    payment_methods = PaymentMethods.objects.filter(business_id = business)
    payment_methods_count = payment_methods.count()
    if request.method =='POST':
        if type =='amenities':
            if(amenities_count == 0 ):
                form = BusinessAmenitiesForm(request.POST)
                if form.is_valid:
                    form = form.save(commit=False)
                    form.business_id = business
                    form.save()
                    messages.success(request,'your business amenities are added successfully')
                    return redirect('bus.options')
            else:
                form = BusinessAmenitiesForm(request.POST,instance=amenities.first())
                form.save()
                messages.success(request,'your business amenities are updated')
        elif type == 'payment_methods':
            if payment_methods_count == 0 :
                form = BusinessPaymentMethodsForm(request.POST)
                if form.is_valid:
                    form = form.save(commit=False)
                    form.business_id = business
                    form.save()
                    messages.success(request,'your payment methods are added successfully')
            else:
                form = BusinessPaymentMethodsForm(request.POST,instance=payment_methods.first())
                if form.is_valid:
                    form.save()
                    messages.success(request,'your business payment methods are updated')
    context = {'amenities':amenities.first(),'payment_methods':payment_methods.first()}
    return render(request,'business/options.html',context)
def services(request):
    context = {'page_title':'Business Services'}
    return render(request,'business/services.html',context);