from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Amenities, Business, PaymentMethods, Photos
from business import models


class BusinessProfileForm(ModelForm):
    class Meta:
        model = Business
        fields = ['business_name','business_phone','business_email','business_bio','instagram_link','facebook_link','twitter_link','website','postcode','address_line_1','address_line_2','town','country']
    def __init__(self,*args,**kwargs):
        super(BusinessProfileForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + field.label})
    
class BusinessAmenitiesForm(ModelForm):
    class Meta:
        model= Amenities
        fields =['cus_parking','card_accept','disability','child_friendly','pet_friendly','wifi','loyalty_program']
       
    def __init__(self,*args,**kwargs):
        super(BusinessAmenitiesForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-check-input'})

class BusinessPaymentMethodsForm(ModelForm):
    class Meta:
        model = PaymentMethods
        fields = ['cash','physical','check','paypal','bank_transfer','gift_card']
    def __init__(self,*args,**kwargs):
        super(BusinessPaymentMethodsForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-check-input'})

class BusinessPhotosForm(ModelForm):
    class Meta:
        model = Photos
        fields = ['logo','banner','display_1','display_2','display_3','display_4']
    def __init__(self,*args,**kwargs):
        super(BusinessPhotosForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-check-input'})