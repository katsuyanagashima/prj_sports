from django import forms

from django.forms import ModelForm
from .models import Mst_Heya

class Mst_HeyaForm(forms.ModelForm):
    class Meta:
        model = Mst_Heya
        fields = ('Heya_code', 'Heya_official_kanji', 'Heya_official_kana', 'Heya_kanji_2char', 'Heya_kanji_3char',)
