from django import forms
from bootstrap3_datetime.widgets import DateTimePicker

class ServiceEventForm2(forms.Form):
	service_date = forms.DateField(
                widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                               "pickTime": False}))
class ServiceEventForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
