from django import forms
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe
from datetime import date, datetime


class BootstrapDateTimeInput(forms.DateTimeInput):
    class Media:
        js = (
            settings.STATIC_URL + 'bootstrap/js/bootstrap-datetimepicker.min.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'bootstrap/css/bootstrap-datetimepicker.min.css',
            )
        }

    def render(self, name, value, attrs=None):
        if value:
            if isinstance(value, date):
                value = datetime(value.year, value.month, value.day)
            if isinstance(value, datetime):
                value = value.strftime('%d/%m/%Y %H:%M:%S')
        else:
            value = ''
            
        lang = translation.get_language()
        lang = "%s-%s" % (lang.split('-')[0].lower(), lang.split('-')[1].upper()) if '-' in lang else lang

        output = '''
        <div id="id_%(name)s" class="input-append date" data-bootstrap-widget="datetimepicker">
            <input value="%(value)s" name="%(name)s" data-format="dd/MM/yyyy hh:mm:ss" type="text"></input>
            <span class="add-on">
                <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
            </span>
        </div>
        <script type="text/javascript">
        $(function() {
           $('#id_%(name)s').datetimepicker({
           language: '%(lang)s',
           maskInput: true,           // disables the text input mask
           pickDate: true,            // disables the date picker
           pickTime: true,            // disables de time picker
           pick12HourFormat: false,   // enables the 12-hour format time picker
           pickSeconds: true,         // disables seconds in the time picker
           startDate: -Infinity,      // set a minimum date
           endDate: Infinity          // set a maximum date
         });
        });
        </script>
        ''' % {'name':name, 'value':value, 'lang': lang}

        return mark_safe(output)


class BootstrapDateInput(forms.DateTimeInput):
    class Media:
        js = (
            settings.STATIC_URL + 'bootstrap/js/bootstrap-datetimepicker.min.js',
        )
        css = {
            'screen': (
                settings.STATIC_URL + 'bootstrap/css/bootstrap-datetimepicker.min.css',
            )
        }

    def render(self, name, value, attrs=None):
        if value:
            if isinstance(value, date):
                value = datetime(value.year, value.month, value.day)
            if isinstance(value, datetime):
                value = value.strftime('%d/%m/%Y')
        else:
            value = ''
            
        lang = translation.get_language()
        lang = "%s-%s" % (lang.split('-')[0].lower(), lang.split('-')[1].upper()) if '-' in lang else lang

        output = '''
        <div id="id_%(name)s" class="input-append date" data-bootstrap-widget="datetimepicker">
            <input value="%(value)s" name="%(name)s" data-format="dd/MM/yyyy" type="text"></input>
            <span class="add-on">
                <i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>
            </span>
        </div>
        <script type="text/javascript">
        $(function() {
           $('#id_%(name)s').datetimepicker({
           language: '%(lang)s',
           pickTime: false,            // disables de time picker
         });
        });
        </script>
        ''' % {'name':name, 'value':value, 'lang': lang}

        return mark_safe(output)
