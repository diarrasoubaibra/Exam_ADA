from django import forms
from restaurent.models.menu import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'