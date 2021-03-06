from django import forms
from django.core.exceptions import ValidationError
import re


class DayReportForm(forms.Form):
    """
    Description:
    This is a form to capture a date *string* from a Bootstrap 4 datepicker on the index.html page.
    The form then validates this date based on it's length and that it meets the correct pattern.

    Fields:
    day_selected: a char field to take in a date string

    Returns:
    Returns a dict of values of parsed year, month, and day
    """

    day_selected = forms.CharField(required=True, max_length=10)

    def __init__(self, *args, **kwargs):
        super(DayReportForm, self).__init__(*args, **kwargs)

    def clean_day_selected(self):
        day_selected = self.cleaned_data['day_selected']

        if len(day_selected) != 10:
            raise ValidationError("You entered an invalid date for this field.")

        if not re.match('^(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4}).*?$', day_selected):
            raise ValidationError("You entered an invalid date for this field.")

        year = day_selected.split("/")[2]
        day = day_selected.split("/")[1]
        month = day_selected.split("/")[0]

        return {'year': year, 'month': month, 'day': day}

    def clean(self):
        super(DayReportForm, self).clean()
        return self.cleaned_data


class MonthReportForm(forms.Form):
    """
    Description:
    This is a form to capture a date *string* from a Bootstrap 4 datepicker on the index.html page.
    The form then validates this date based on it's length and that it meets the correct pattern.

    Fields:
    day_selected: a char field to take in a date string

    Returns:
    Returns a dict of values of parsed year, month, and day
    """

    month_selected = forms.CharField(required=True, max_length=7)

    def __init__(self, *args, **kwargs):
        super(MonthReportForm, self).__init__(*args, **kwargs)

    def clean_month_selected(self):
        month_selected = self.cleaned_data['month_selected']

        if len(month_selected) != 7:
            raise ValidationError("You entered an invalid date for this field.")

        if not re.match('^(?P<month>\d{2})/(?P<year>\d{4}).*?$', month_selected):
            raise ValidationError("You entered an invalid date for this field.")

        year = month_selected.split("/")[1]
        month = month_selected.split("/")[0]

        return {'year': year, 'month': month}

    def clean(self):
        super(MonthReportForm, self).clean()
        return self.cleaned_data


