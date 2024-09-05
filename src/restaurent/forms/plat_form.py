from django import forms
from restaurent.models.plat import Plat

class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = '__all__'
