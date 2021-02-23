from django import forms

from .models import Place


class RideForm(forms.Form):
    class Meta:
        model = Place
        fields = ('source', 'destination', 'date', 'number', 'time', 'location')
        widgets = {'source': forms.TextInput(attrs={'class': 'form-control'}),
                   'destination': forms.TextInput(attrs={'class': 'form-control'}),
                   'date': forms.DateInput(attrs={'class': 'form-control'}),
                   'number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'time': forms.TextInput(attrs={'class': 'form-control'}),
                   'location': forms.TextInput(attrs={'class': 'form-control'}),
                   }
