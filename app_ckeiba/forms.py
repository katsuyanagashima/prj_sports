from django import forms
from .models import Tran_Systemstatus

# class Tran_SystemstatusForm(forms.ModelForm):
#     class Meta:
#         model = Tran_Systemstatus
#         fields = ('Unyou_date', 'SystemStatus')

# class Tran_SystemstatusForm(forms.Form):
#     SystemStatus = forms.CharField(
#         label='タイトル',
#         max_length=200,
#         required=True,
#     )

# class HelloForm(forms.Form):
#     your_name = forms.CharField(
#         label='名前',
#         max_length=20,
#         required=True,
#         widget=forms.TextInput()
#     )