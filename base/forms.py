from django import forms
#from django.contrib.admin.widgets import AdminDateWidget
from base.models import Custadv, Custqtn


class CustadvForm(forms.ModelForm):
    cuno = forms.CharField(label='客戶代號', min_length=6, max_length=10, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    ipntfy = forms.CharField(label='應通知公司', max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    ipntfym = forms.CharField(label='貨主聯絡人', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    ipntftl = forms.CharField(label='電話號碼', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    ipntffx = forms.CharField(label='傳真號碼', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    ipmnspay = forms.BooleanField(label='是否月結', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), required=False)
    ipentry = forms.BooleanField(label='是否報關', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), required=False)
    iprtord = forms.BooleanField(label='是否進口指定貨', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), required=False)
    ipntfmk = forms.CharField(label='備註', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Custadv
        fields = ['cuno', 'ipntfy', 'ipntfym', 'ipntftl', 'ipntffx', 'ipmnspay', 'ipentry', 'iprtord', 'ipntfmk',]

class CustqtnForm(forms.ModelForm):

    org = forms.CharField(label='ORG', max_length=3, widget=forms.TextInput(attrs={'class':'form-control'}))
    qtndd = forms.DateField(label='日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}))
    qtns = forms.CharField(label='說明', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Custqtn
        fields = ['org', 'qtndd', 'qtns',]
