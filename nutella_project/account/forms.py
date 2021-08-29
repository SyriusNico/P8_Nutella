from django import forms

class NameForm(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    email = forms.CharField(label='user_name', max_length=100)