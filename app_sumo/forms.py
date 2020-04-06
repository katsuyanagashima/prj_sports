from django import forms

from django.forms import ModelForm
from .models import Mst_Heya
from .models import Mst_Event
from .models import Mst_Rikishi
from django.contrib.admin.widgets import AdminDateWidget

STATUS_CHOICES = (
    ('activeDuty', '現役'),
    ('notActiveDuty', '現役以外'),
)

class Mst_HeyaForm(forms.ModelForm):
    class Meta:
        model = Mst_Heya
        fields = ('Heya_code', 'Heya_official_kanji', 'Heya_official_kana', 'Heya_kanji_2char', 'Heya_kanji_3char',)

class Mst_Event_Form(forms.ModelForm):
    
    class Meta:
        model = Mst_Event
        fields = ('Event_date', 'Torikumi_nichime_code', 'Shoubu_nichime_code', 'Basho_code', 'Frist_date', 'Banzuke_date', 'Age_calcu_reference_date')

class SearchRikishilistForm(forms.Form):
    status_chk = forms.ChoiceField(
        label = 'ステータス',
        widget=forms.CheckboxSelectMultiple(),
        choices=STATUS_CHOICES,
        required=False,
    )


class Mst_RikishiForm(forms.ModelForm):
    
    class Meta:
        model = Mst_Rikishi
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Mst_RikishiForm, self).__init__(*args, **kwargs)
        self.fields['Date_of_birth'].required = True
        self.fields['Date_of_birth'].widget.attrs = {'placeholder': 'yyyy-mm-dd'}