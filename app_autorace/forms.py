from django import forms

from .models import csvtest1

class Csvtest1Form(forms.ModelForm):

    class Meta:
        model = csvtest1
        fields = ('no', 'name',)