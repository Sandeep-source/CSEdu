from django import forms
from franchise.models import Franchise

class FranciseForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = (
            'centre_name',
            'address1',
            'address2',
            'city',
            'state',
            'pincode',
            'email',
            'head_name',
            'phone_number',
            'head_email_address'
        )
        widgets  = {
            'centre_name': forms.TextInput(attrs={'class':'form-control',"label":"Hello"})
        }
        labels = {
            "centre_name": "Hello"
        }