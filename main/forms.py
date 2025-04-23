from django import forms
from .models import Enquiry  # Ensure this import is correct
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry 
        # Specify the model
        
        # Or list specific fields: ['full_name', 'email', 'subject', 'message', 'send_location']
        fields = '__all__'

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2'] 