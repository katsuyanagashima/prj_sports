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

# コーナー・ラップフォームセット
class Md_Corner_RapForm(forms.ModelForm):
    class Meta:
        model = Md_Corner_Rap
        fields = '__all__'
Corner_RapFormset = forms.modelformset_factory(
    Md_Corner_Rap, form=Md_Corner_RapForm, extra=0
)

# 上がりフォームセット
class Md_AgariForm(forms.ModelForm):
    class Meta:
        model = Md_Agari
        fields = '__all__'
AgariFormset = forms.modelformset_factory(
    Md_Agari, form=Md_AgariForm, extra=0
)

# 通信文フォームセット
class Md_TsuushimbunForm(forms.ModelForm):
    class Meta:
        model = Md_Tsuushimbun
        fields = '__all__'
TsuushimbunFormset = forms.modelformset_factory(
    Md_Tsuushimbun, form=Md_TsuushimbunForm, extra=0
)

# 入場人員フォームセット
class Md_NyujoForm(forms.ModelForm):
    class Meta:
        model = Md_Nyujo
        fields = '__all__'
NyujoFormset = forms.modelformset_factory(
    Md_Nyujo, form=Md_NyujoForm, extra=0
)

# 売上金フォームセット
class Md_UriagekinForm(forms.ModelForm):
    class Meta:
        model = Md_Uriagekin
        fields = '__all__'
UriagekinFormset = forms.modelformset_factory(
    Md_Uriagekin, form=Md_UriagekinForm, extra=0
)


#出走表用フォームセット
ShussouhyouFormset = forms.inlineformset_factory(
    Md_Shussouhyou ,Md_Shussouhyou_shussouba, fk_name='shussouhyou',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#出走表用フォームセット過去5成績用
class Md_Shussouhyou_shussouba_5seisekiForm(forms.ModelForm):
    class Meta:
        model = Md_Shussouhyou_shussouba_5seiseki
        fields = '__all__'
Shussouhyou_shussouba_5seiseki_Formset = forms.modelformset_factory(
    Md_Shussouhyou_shussouba_5seiseki, form=Md_Shussouhyou_shussouba_5seisekiForm, extra=0
)

#出走表用フォームセット場別距離別累計成績用
class Md_Shussouhyou_shussouba_ruikeiForm(forms.ModelForm):
    class Meta:
        model = Md_Shussouhyou_shussouba_ruikei
        fields = '__all__'
Shussouhyou_shussouba_ruikei_Formset = forms.modelformset_factory(
    Md_Shussouhyou_shussouba_ruikei, form=Md_Shussouhyou_shussouba_ruikeiForm, extra=0
)





#成績払戻用フォームセット成績
seiseki_haraimodoshiFormset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_seiseki, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)




#成績払戻用フォームセット単勝
seiseki_haraimodoshi_tan_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_tan, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット複勝
seiseki_haraimodoshi_fuku_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_fuku, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット枠複
seiseki_haraimodoshi_wakupuku_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_wakupuku, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット枠単
seiseki_haraimodoshi_wakutan_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_wakutan, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット馬複
seiseki_haraimodoshi_umapuku_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_umapuku, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット馬単
seiseki_haraimodoshi_umatan_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_umatan, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット三連複
seiseki_haraimodoshi_sanpuku_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_sanpuku, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセット三連単
seiseki_haraimodoshi_santan_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_santan, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)

#成績払戻用フォームセットワイド
seiseki_haraimodoshi_wa_Formset = forms.inlineformset_factory(
    Md_Seiseki_Haraimodoshi ,Md_Seiseki_Haraimodoshi_wa, fk_name='seiseki_haraimodoshi',
    fields='__all__',
    extra=0,
    max_num=16,
    can_delete=True
)
