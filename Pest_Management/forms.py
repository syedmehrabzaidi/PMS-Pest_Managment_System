from django import forms
from .models import Pest_table

class update_edit_form(forms.ModelForm):
    class Meta:
     model = Pest_table
     fields = ['name','pesttype','tl','tu','dd']
     widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'pesttype': forms.TextInput(attrs={'class':'form-control'}),
      'tl': forms.TextInput(attrs={'class':'form-control'}),
      'tu': forms.TextInput(attrs={'class':'form-control'}),
      'dd': forms.TextInput(attrs={'class':'form-control'}),
     }