from django import forms

from django.forms import ModelForm
from .models import Mst_Heya
from .models import Mst_Event

class Mst_HeyaForm(forms.ModelForm):
    class Meta:
        model = Mst_Heya
        fields = ('Heya_code', 'Heya_official_kanji', 'Heya_official_kana', 'Heya_kanji_2char', 'Heya_kanji_3char',)

class Mst_Event_Form(forms.ModelForm):
    
    class Meta:
        model = Mst_Event
        fields = ('Event_date', 'Torikumi_nichime_code', 'Shoubu_nichime_code', 'Basho_code', 'Frist_date', 'Banzuke_date', 'Age_calcu_reference_date')

