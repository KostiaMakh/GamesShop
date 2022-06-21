from django import forms
from .models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, label='First name',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=128, label='Last name',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=256, label='Email address',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=128, label='Contact phone number',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=256, label='Delivery address',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=128, label='City',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal_code = forms.IntegerField(label='Postal code',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'city',
            'address',
            'postal_code',
        )
