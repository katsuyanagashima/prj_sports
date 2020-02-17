from django import forms

from django.forms import ModelForm
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('player1', 'outcome1', 'waza', 'outcome2', 'player2',)