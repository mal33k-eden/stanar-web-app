from django.db.models import fields
from django.forms import ModelForm
from .models import Business


class BusinessProfileForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name','phone','email','bio','instagram','facebook','twitter','website','postcode','address1','address2','town','country']
    def __init__(self,*args,**kwargs):
        super(BusinessProfileForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + field.label})
    