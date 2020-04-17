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








