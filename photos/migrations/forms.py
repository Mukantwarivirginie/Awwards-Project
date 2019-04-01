from django import forms
from .models import Profile,Image


class Awwards-projectForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date','editor']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date','like']
        


