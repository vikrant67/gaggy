from django.contrib.auth.models import User
from .models import Upload 
from django import forms 

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['first_name','username','password','email']
class UploadForm(forms.ModelForm):
    
    
    class Meta:
        model = Upload
        fields=['description','media']