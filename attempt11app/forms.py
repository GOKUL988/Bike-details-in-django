from django import forms
from .models import bike
class bikeform(forms.ModelForm):
    class Meta:
        model=bike
        fields=[
            "bikename",
            "bikeserial"
        ]