# encoding: utf-8

# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from patients.models import *
from patients.forms import PatientForm

class PatientListView(ListView):
    queryset = Patient.objects.all()
    context_object_name = 'patients'
    template_name = 'patient_list.html'    

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        print context
        return context

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'patient_detail.html'    

class PatientCreateView(CreateView):
    form_class = PatientForm
    template_name = 'patient_create_form.html'
    success_url = '/patients/'

    def form_valid(self, form):
        self.patient = form.save(commit=False)
        self.patient.record_by = self.request.user.get_profile()
        return super(PatientCreateView, self).form_valid(form)

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_update_form.html'
    success_url = '/patients/'
    context_object_name = 'patient'

    # def form_valid(self, form):
    #     self.patient = form.save(commit=False)
    #     self.patient.lastupdate_by = self.request.user.get_profile()
    #     self.success_url = reverse('patient-detail', args=self.kwargs['pk'])
    #     return super(PatientUpdateView, self).form_valid(form)

class PatientDeleteView(DeleteView):
    model = Patient
    form_class = PatientForm
    success_url = '/patients/'
    context_object_name = 'patient'
