from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError

# from .models import Applicant

def validate_checked(value):
    if not value:
        raise ValidationError("Required.")

class ContactUsForm(forms.Form):
    YEARS = range(datetime.now().year, datetime.now().year+2)
    
    first_name = forms.CharField(
       widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )

    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true.',
        validators=[validate_checked]
    )