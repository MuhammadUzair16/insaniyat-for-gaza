from django import forms
from .models import UserReport

class ReportForm(forms.ModelForm):
    class Meta:
        model = UserReport
        fields = ['evidence']
        widgets = {
            'evidence': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Link to evidence (news article, official document)'
            })
        }