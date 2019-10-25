from django import forms
from .models import Profile,Project,Rate
from .models import *

# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['', '']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['upload_by','likes','profile']
               
class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude=['username','project','control']

