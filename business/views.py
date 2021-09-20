from business import forms
from business.models import Amenities, Business, PaymentMethods, Photos
from django.db.models.expressions import F
from business.forms import BusinessAmenitiesForm, BusinessPaymentMethodsForm, BusinessPhotosForm, BusinessProfileForm
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
    amenities = Amenities.objects.filter(business_id = business.id)
    amenities_count = amenities.count()
    payment_methods = PaymentMethods.objects.filter(business_id = business.id)
    payment_methods_count = payment_methods.count()
    if request.method =='POST':
        if type =='amenities':
            form = BusinessAmenitiesForm(request.POST)
            if form.is_valid:
                if(amenities_count == 0 ):
                    form = form.save(commit=False)
                    form.business_id = business.id
                    form.save()
                    messages.success(request,'your business amenities are added successfully')
                    return redirect('bus.options')
                else:
                    amenity = amenities.first()
                    amenity.cus_parking = request.POST.get('cus_parking','off')
                    amenity.card_accept = request.POST.get('card_accept','off')
                    amenity.child_friendly = request.POST.get('child_friendly','off')
                    amenity.disability = request.POST.get('disability','off')
                    amenity.wifi = request.POST.get('wifi','off')
                    amenity.loyalty_program = request.POST.get('loyalty_program','off')
                    amenity.pet_friendly = request.POST.get('pet_friendly','off')
                    amenity.save()
                    messages.success(request,'your business amenities are updated')
                    return redirect('bus.options')
        elif type == 'payment_methods':
            form = BusinessPaymentMethodsForm(request.POST)
            if form.is_valid:
                if payment_methods_count == 0 :
                    form = form.save(commit=False)
                    form.business_id = business.id
                    form.save()
                    messages.success(request,'your payment methods are added successfully')
                    return redirect('bus.options')
                else:
                    method = payment_methods.first()
                    method.cash = request.POST.get('cash','off')
                    method.physical = request.POST.get('physical','off')
                    method.check = request.POST.get('check','off')
                    method.paypal = request.POST.get('paypal','off')
                    method.gift_card = request.POST.get('gift_card','off')
                    method.bank_transfer = request.POST.get('bank_transfer','off')
                    method.save()
                    messages.success(request,'your business payment methods are updated')
                    return redirect('bus.options')
    context = {'page_title':'Business Options','amenities':amenities.first(),'payment_methods':payment_methods.first()}
    return render(request,'business/options.html',context)

def photos(request):
    user = request.user.id
    business = Business.objects.filter(user_id=user).first()
    bus_photos = Photos.objects.filter(business_id=business.id)
    bus_photos_count = bus_photos.count()
    if request.method =='POST':
        if bus_photos_count > 0:
            form = BusinessPhotosForm(request.POST,request.FILES, instance=bus_photos)
        if bus_photos_count == 0:
            form = BusinessPhotosForm(request.POST,request.FILES)
        if form.is_valid:
            if bus_photos_count == 0:
                form = form.save(commit=False)
                form.business_id = business.id
            form.save()

    context = {'page_title':'Business Photos',}
    return render(request, 'business/photos.html',context)

def services(request):
    context = {'page_title':'Business Services'}
    return render(request,'business/services.html',context);