from django import forms
from .models import DeviceInField, Order

class DeviceInFieldForm(forms.ModelForm):
    class Meta:
        model = DeviceInField
        fields = ['serial_number', 'customer', 'device', 'owner']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'device': forms.Select(attrs={'class': 'form-control'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['device', 'customer', 'order_description', 'order_status']
        widgets = {
            'device': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}),
        }
