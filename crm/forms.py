from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'css_input'}))
    phone = forms.CharField(max_length=250)