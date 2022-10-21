from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Your Message', widget=forms.Textarea(attrs={'class': 'form-control'}))
