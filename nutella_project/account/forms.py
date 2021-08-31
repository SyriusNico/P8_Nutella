from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    
    # Form's field
    username = forms.CharField(label=("Nom d'utilisateur"))
    password1 = forms.CharField(label=("Mot de passe"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer', widget=forms.PasswordInput)
    email = forms.EmailField()

    # Confirm the password
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Le mot de passe incorect")

        return password2

    # Store the user
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
