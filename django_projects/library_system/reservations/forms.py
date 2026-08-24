from django import forms
from .models import Reservation
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['book', 'member', 'reserved_date']
        widgets = {
            'reserved_date': forms.DateInput(attrs={'type': 'date'}),
        }
