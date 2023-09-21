from django.forms import ModelForm
from student.models import Frencise

class FranciseForm(ModelForm):
    class Meta:
        model = Frencise
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