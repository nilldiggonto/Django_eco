
from django.forms import ModelForm, Textarea,TextInput,CharField,Select
from .models import Address

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            # 'billing_profile',
            # 'address_type',
            'address_line_1',
            'address_line_2',
            'country',
            'city',
            'state',
            'postal_code'
        ]

        # widgets = {
        #     'billing_profile':Select(attrs={'class':'form-control','id':'form-control'}),
        #     # 'address_type'
        # }





        #  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'form-control','placeholder':'username'}))