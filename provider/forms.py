from django import forms
from .models import Provider

class RegistrationForm(forms.ModelForm):
    password = forms.CharField()
    confirm_password = forms.CharField()
    class Meta:
        model = Provider
        fields = ['first_name','last_name', 'email', 'username', 'password']
        labels = {
            'password': 'Password','confirm_password': 'Confirm Password'
        }
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            placeholder = name.replace('_',' ').title()
            field.widget.attrs.update({'class':'form-control','placeholder':'Enter ' + placeholder})