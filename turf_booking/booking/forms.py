from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'booking_date', 'time_slot']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(choices=[
                ('6am-7am', '6:00 AM - 7:00 AM (500/-)'),
                ('7am-8am', '7:00 AM - 8:00 AM (750/-)'),
                ('8am-9am', '8:00 AM - 9:00 AM (1000/-)'),
            ])
        }
from django import forms

class CancelBookingForm(forms.Form):
    phone = forms.CharField(max_length=10, label="Enter your phone number")
