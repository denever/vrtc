from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from accounts.views import *

urlpatterns = patterns('accounts.views',
		       url(r'^profile/$',
			   login_required(ProfileView.as_view()),
			   name='profile'
		       ),
		       url(r'^settype/(?P<type>\w)/$',
			   login_required(UserSetTypeView.as_view()),
			   name='user-settype'
		       ),
		   )
