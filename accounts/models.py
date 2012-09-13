from django.db import models

# importing User for UserProfile
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.core.mail import mail_admins
from django.dispatch import receiver

from registration.signals import user_activated

# Create your models here.
class UserProfile(models.Model):
    user_types = (
	(u'D', _(u'Doctor')),
	(u'P', _(u'Patient')),
	)

    user = models.ForeignKey(User, unique=True)
    user_type = models.CharField(_('Type'), max_length=2, choices=user_types, null=True)

    def __unicode__(self):
	return '%s <%s>' % (self.user.username, self.user.email)

    class Meta:
	verbose_name = _('Account')
	verbose_name_plural = _('Account')

# callback on user activated to create a userprofile after activation
@receiver(user_activated)
def user_activated_cb(sender, **kwargs):
    u = kwargs['user']
    up = UserProfile(user=u)
    up.save()
    mail_admins('New user registerd', 'User: %s i registered' % up)
