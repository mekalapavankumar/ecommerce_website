from django import forms
from django.core.exceptions import ValidationError
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''
def isShort(self):
        short = self.cleaned_data['prdname']
        if len(short)<4:
            raise ValidationError("Too Small Name")
        
class ProductForm(forms.Form):

    pid = forms.IntegerField(required=True,help_text='Product id')
    prdname = forms.CharField(widget=forms.TextInput())
    price = forms.IntegerField(help_text='Product Price')
    Manufacture = forms.DateField(widget=forms.SelectDateWidget,required=False)
    
    def clean_price(self):
        data = self.cleaned_data['price']
        if data <0:
            raise ValidationError('Price should not be negative')
        return data
    def clean_prdname(self):
        d = self.cleaned_data['prdname']
        if len(d)<4:
            raise ValidationError("Too Small Name")
        return d
'''
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_staff']
