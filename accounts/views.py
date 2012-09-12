# Create your views here.
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.utils import simplejson

from accounts.models import UserProfile

class ProfileView(TemplateView):
    template_name = "profile.html"
