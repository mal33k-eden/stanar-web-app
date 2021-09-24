from accounts.forms import StaffRegistrationForm
from django.contrib.messages.api import error
import business
from services.models import Category
from business import forms
from django.core.exceptions import ValidationError
from business.models import Amenities, Business, PaymentMethods, Photos, Service, Staff, StaffService
from django.db.models.expressions import F
from business.forms import BusinessAmenitiesForm, BusinessPaymentMethodsForm, BusinessPhotosForm, BusinessProfileForm, BusinessServiceForm
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
    bus_photos=[]
    business = Business.objects.filter(user_id=user).first()
    bus_photos_2 = Photos.objects.filter(business_id=business.id)
    bus_photos_count = bus_photos_2.count()
    if bus_photos_count > 0 :
        bus_photos = Photos.objects.get(business_id=business.id)
    if request.method =='POST':
        if bus_photos_count > 0:
            form = BusinessPhotosForm(request.POST,request.FILES, instance=bus_photos)
        if bus_photos_count == 0:
            form = BusinessPhotosForm(request.POST,request.FILES)
        if form.is_valid:
            print(form.clean)
            if bus_photos_count == 0:
                form = form.save(commit=False)
                form.business_id = business.id
            form.save()
            messages.success(request,'your photo uploaded successfully')
            return redirect('bus.photos')
    context = {'page_title':'Business Photos','photos':bus_photos}
    return render(request, 'business/photos.html',context)

def services(request,pk=''):
    form = BusinessServiceForm()
    user = request.user.id
    business = Business.objects.filter(user_id=user).first()
    categories = Category.objects.all()
    if request.method =='POST':
        form = BusinessServiceForm(request.POST)
        form_service =request.POST.get('service')
        bus_services = Service.objects.filter(service_id=form_service)
        if bus_services.count() < 1:
            if form.is_valid():
                form = form.save(commit=False)
                form.business_id = business.id
                form.save()
                messages.success(request,'service added to your profile')
                BusinessServiceForm()
                return redirect('bus.services')
            else:
                messages.error(request,'form not correctly filled')
        else:
            messages.error(request,'ERROR: selected service already added to your profile')
    context = {'page_title':'Business Services','form':form,'categories':categories,'business':business,'error':error}
    return render(request,'business/services.html',context)

def updateService(request,pk):
    service = Service.objects.get(id=pk)
    if request.method =='POST':
        form = BusinessServiceForm(request.POST,instance=service)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'service updated')
            return redirect('bus.services')
    return redirect('bus.services')
def deleteService(request,pk):
    service = Service.objects.get(id=pk)
    if request.method =='POST':
        service.delete()
        messages.success(request,'service removed from your profile')
    return redirect('bus.services')
def staff(request):
    user = request.user.id
    biz = Business.objects.filter(user_id=user).first()
    bus_services = Service.objects.filter(business_id=biz.id)
    form = StaffRegistrationForm()
    if request.method=='POST':
        form = StaffRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            instance_account = form.save()
            staff = Staff.objects.create(user=instance_account,business=biz)
            staff.save()
            services = request.POST.getlist('service')
            for service in services:
                staffService = StaffService.objects.create(staff=staff,service_id= service,is_active=True)
                staffService.save()
            messages.success(request,'Staff added successfully')
            return redirect('bus.staff')
    context ={'page_title':'Business Staff','services':bus_services,'form':form,'business':biz}
    return render(request,'business/staff.html',context)
def deleteStaff(request):
    return render(request,'business/staff.html')
def updateStaff(request):
    return render(request,'business/staff.html')
