from django import forms
from .models import Profile,Project,Grade
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['username']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['upload_by','likes','profile']
               
class GradeForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['username','project','total','avg']


        

