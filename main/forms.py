from django import forms
from .models import Enquiry, Trainer  # Ensure this import is correct
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User, Group

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

class profileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class changepasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password': forms.PasswordInput(),
            'new_password1': forms.PasswordInput(),
            'new_password2': forms.PasswordInput(),
        }


#trainer forms
class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model =Trainer
        fields = ['UserName', 'password']
        widgets = {
            'UserName': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(),
            
        }
        
 #trainer profile form
class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['full_name','email', 'phone','img','facebook','instagram','twitter','youtube']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
          
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'img': forms.ClearableFileInput(attrs={'placeholder': 'Profile Picture'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Facebook URL'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Instagram URL'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Twitter URL'}),
            'youtube': forms.TextInput(attrs={'placeholder': 'YouTube URL'}),
        }
       