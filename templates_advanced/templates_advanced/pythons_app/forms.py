from .models import Python
from django import forms


class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = '__all__'
