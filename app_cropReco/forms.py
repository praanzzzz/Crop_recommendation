from django import forms
from .models import Crop_models
class CropForms(forms.ModelForm):
    class Meta:
        model = Crop_models
        fields = ['Nitrogen', 'Phosphorus','Potassium','Temperature', 'Humidity', 'pH', 'Rainfall']