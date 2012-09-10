from django import forms
from django.utils.translation import ugettext as _
from patients.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
