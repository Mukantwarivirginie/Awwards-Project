from django import forms
from .models import Profile,Project


class SignUpForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date','editor']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date','like']

        








  

