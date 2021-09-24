from business.models import Staff
from django.forms import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name','email','password1','password2','policy_agreed']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        labels={
            'policy_agreed':'Terms and Conditions'
        }
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            if(name =='policy_agreed'):
                field.widget.attrs.update({'class':'form-check-input'})
            else:
                field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + field.label})
    def save(self, commit= False):
        user = super().save(commit)
        user.is_provider = True
        user.is_active = True
        user.save()

class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name','email','password1','password2','username']
    def __init__(self,*args,**kwargs):
        super(StaffRegistrationForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + field.label})
    def save(self, commit= False):
        user = super().save(commit)
        user.is_staff = True
        user.is_active = True
        user.policy_agreed= True
        user.username = user.username.lower()
        user.save()
        return user;
