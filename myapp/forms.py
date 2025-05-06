from django import forms
from .models import User
# from .models import ContactForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email','phone','services','message']

