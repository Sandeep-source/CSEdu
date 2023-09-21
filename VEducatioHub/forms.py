from django.forms import ModelForm
from franchise.models import Franchise

class FranciseForm(ModelForm):
    class Meta:
        model = Franchise
        fields = [
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
        ]