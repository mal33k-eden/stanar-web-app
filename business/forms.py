from django.db.models import fields
from django.forms import ModelForm
from .models import Business


class BusinessProfileForm():
    class Meta:
        model = Business
        fields = ['name','phone','email','bio','instagram','facebook','twitter','youtube','website','postcode','address1','address2','town','country']
        labels={
            'name':'Business Name',
            'address1':'Address Line 1',
            'address2':'Address Line 2 (Optional)',
            'town':'Town/City',
        }
        def __init__(self,*args,**kwargs):
            super(BusinessProfileForm,self).__init__(*args,**kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + field.label})