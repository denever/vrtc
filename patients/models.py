from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Patient(models.Model):
    gender_choices = (
        (u'M', _(u'Male')),
        (u'F', _(u'Female')),
        )

    name = models.CharField(_('Name'), max_length=200)
    surname = models.CharField(_('Name'), max_length=200)
    birth_date = models.DateField(_('Birth date'))
    gender = models.CharField(_('Gender'), max_length=2, choices=gender_choices)
    address = models.CharField(_('Address'), max_length=200)
    diagnosis = models.TextField(_('Diagnosis'))
    diagnosis_date = models.DateField(_('Date of Diagnosis'))
    previous_location = models.CharField(_('Address'), max_length=200)
    job = models.CharField(_('Job'), max_length=200)
    hse = models.CharField(_('Harmful substance exposition'), max_length=200)

    def __unicode__(self):
        return "%s: %s %s" % (_("Patient"), self.surname, self.name)

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
