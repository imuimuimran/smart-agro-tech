from django import forms
import re
from .models import Order

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Your Name')
    mobile = forms.CharField(
        max_length=14,
        label='Your Mobile Number',
        help_text='Format: 01XXXXXXXXX or +8801XXXXXXXXX',
    )
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        pattern = r'^(?:\+8801|8801|01)[0-9]{9}$'
        if not re.match(pattern, mobile):
            raise forms.ValidationError("Enter a valid Bangladeshi mobile number.")
        return mobile
    

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'mobile': forms.TextInput(attrs={'required': True}),
            'address_village': forms.TextInput(attrs={'required': True}),
            'address_union': forms.TextInput(attrs={'required': True}),
            'address_post': forms.TextInput(attrs={'required': True}),
            'address_thana': forms.TextInput(attrs={'required': True}),
            'address_district': forms.TextInput(attrs={'required': True}),
            'delivery_village': forms.TextInput(attrs={'required': True}),
            'delivery_union': forms.TextInput(attrs={'required': True}),
            'delivery_post': forms.TextInput(attrs={'required': True}),
            'delivery_thana': forms.TextInput(attrs={'required': True}),
            'delivery_district': forms.TextInput(attrs={'required': True}),
        }
