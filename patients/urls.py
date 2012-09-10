from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from patients.views import *

urlpatterns = patterns('patients.views',
                       url(r'^$', login_required(PatientListView.as_view()),
                           name='patients'),

                       url(r'^(?P<pk>\d+)/$',
                           login_required(PatientDetailView.as_view()),
                           name = 'patient-detail'),

                       url(r'^create/$',
                           login_required(PatientCreateView.as_view()),
                           name = 'patient-create'
                           ),

                       url(r'^(?P<pk>\d+)/update/$',
                           login_required(PatientUpdateView.as_view()),
                           name = 'patient-edit'
                           ),

                       url(r'^/(?P<pk>\d+)/delete$',
                           login_required(PatientDeleteView.as_view()),
                           name = 'patient-delete'
                           ),
                       )
