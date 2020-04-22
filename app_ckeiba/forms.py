from django import forms
from django.forms import ModelForm
from .models import *

class Mst_HaishinshaForm(forms.ModelForm):
    class Meta:
        model = Mst_Haishinsha
        fields = '__all__'

class Mst_Haishinsaki_NomalForm(forms.ModelForm):
    class Meta:
        model = Mst_Haishinsaki_Nomal
        fields = '__all__'

class Mst_Haishinsaki_LimitedForm(forms.ModelForm):
    class Meta:
        model = Mst_Haishinsaki_Limited
        fields = '__all__'

class Mst_PrinterForm(forms.ModelForm):
    class Meta:
        model = Mst_Printer
        fields = '__all__'

class Mst_Kaisai_HiwariForm(forms.ModelForm):
    class Meta:
        model = Mst_Kaisai_Hiwari
        fields = '__all__'
        
class Mst_Honjitu_ShikouForm(forms.ModelForm):
    class Meta:
        model = Mst_Honjitu_Shikou
        fields = '__all__'
        
class Mst_JouForm(forms.ModelForm):
    class Meta:
        model = Mst_Jou
        fields = '__all__'

class Mst_GradeForm(forms.ModelForm):
    class Meta:
        model = Mst_Grade
        fields = '__all__'

class Mst_Breed_ageForm(forms.ModelForm):
    class Meta:
        model = Mst_Breed_age
        fields = '__all__'

class Mst_WeatherForm(forms.ModelForm):
    class Meta:
        model = Mst_Weather
        fields = '__all__'




# 中間DB

class Md_ShussouhyouForm(forms.ModelForm):
    class Meta:
        model = Md_Shussouhyou
        fields = '__all__'

class Md_Seiseki_HaraimodoshiForm(forms.ModelForm):
    class Meta:
        model = Md_Seiseki_Haraimodoshi
        fields = '__all__'

class Md_Corner_RapForm(forms.ModelForm):
    class Meta:
        model = Md_Corner_Rap
        fields = '__all__'

class Md_AgariForm(forms.ModelForm):
    class Meta:
        model = Md_Agari
        fields = '__all__'

class Md_TshuushinbunForm(forms.ModelForm):
    class Meta:
        model = Md_Tshuushinbun
        fields = '__all__'

class Md_NyujoForm(forms.ModelForm):
    class Meta:
        model = Md_Nyujo
        fields = '__all__'

class Md_UriagekinForm(forms.ModelForm):
    class Meta:
        model = Md_Uriagekin
        fields = '__all__'


#出走表用フォームセット
ShussouhyouFormset = forms.inlineformset_factory(
    Md_Shussouhyou ,Md_Shussouhyou_shussouba, fk_name='shussouhyou',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#出走表用フォームセット過去成績用
Shussouhyou_shussoubaFormset = forms.inlineformset_factory(
    Md_Shussouhyou_shussouba ,Md_Shussouhyou_shussouba_5seiseki, fk_name='shussouhba',
    fields='__all__',
    extra=0,
    max_num=5,
    can_delete=True
)

#成績払戻用フォームセット
seiseki_haraimodoshiFormset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_seiseki, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)