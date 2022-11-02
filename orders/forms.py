from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'city', 'address', 'phone_number', 'delivery_method', 'pay_method']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder': 'Имя'}),
            'last_name':forms.TextInput(attrs={
                'placeholder': 'Фамилия'}),
            'email':forms.TextInput(attrs={
                'placeholder': 'Емаил'}),
            'address':forms.TextInput(attrs={
                'placeholder': 'Адрес доставки'}),
            'phone_number':forms.TextInput(attrs={
                'placeholder': 'Номер телефона'}),
            'city':forms.TextInput(attrs={
                'placeholder': 'Ваше место'}),
            'delivery_method': forms.RadioSelect(attrs={
                'class': 'order-checkbox'}),
            'pay_method': forms.RadioSelect(attrs={
                'class': 'order-checkbox'}),
        }