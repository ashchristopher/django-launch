from django import forms

from launch.models import SignupRequest

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupRequest
        exclude = (
            'active', 
            'invitation_sent', 
            'signed_up',
        )
        