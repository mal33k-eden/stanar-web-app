from django.db.models import fields
from django.forms import ModelForm
from .models import Business


class BusinessProfileForm(ModelForm):
    class Meta:
        model = Business
        fields = ['business_name','business_phone','business_email','business_bio','instagram','facebook','twitter','website','postcode','address_line_1','address_line_2','town','country']
    def __init__(self,*args,**kwargs):
        super(BusinessProfileForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + field.label})
    