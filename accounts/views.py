# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.views.generic import TemplateView
from django.views.generic import View

from django.utils import simplejson

from accounts.models import UserProfile

class ProfileView(TemplateView):
    template_name = "profile.html"

class UserSetTypeView(View):
    def get(self, request, *args, **kwargs):
        up = self.request.user.get_profile()
        try:
            up.user_type =  kwargs['type']
            up.save()
        except Exception, e:
            print e
        return redirect('profile')

    def post(self, request, *args, **kwargs):
        pass
