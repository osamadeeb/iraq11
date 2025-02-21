from django import forms 
from .models import School

class FormSchool(forms.ModelForm):
    class Meta:
        model = School
        fields =['name','country','file','video']

class UpdateFormSchool(forms.ModelForm):
    class Meta:
        model = School
        fields =['name','country','file']