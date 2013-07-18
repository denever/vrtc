from django import forms
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from patients.models import Patient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from patients.widgets import BootstrapDateInput

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('record_by',)
        widgets = {
            'birth_date': BootstrapDateInput(),
            'diagnosis_date': BootstrapDateInput(),
            }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_action = 'patient-create'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Button('cancel', 'Cancel'))        
        super(PatientForm, self).__init__(*args, **kwargs)
