from django import forms
from custcsn.models import Custcsn

class CustcsnForm(forms.ModelForm):
    cuno = forms.CharField(label='客戶代號', min_length=6, max_length=10, required=True, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    CHOICES = (('1','111'),('2','222'),('3','333'))
    cucd = forms.CharField(label='客戶性質', required=True, widget=forms.Select(choices=CHOICES, attrs={'class':'form-control input-sm'}))
    cunme = forms.CharField(label='公司名稱(英)', max_length=40, required=True, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuid = forms.CharField(label='統一編號', max_length=8, required=True, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cunmc = forms.CharField(label='公司名稱(中)', max_length=40, required=True, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuchadd1 = forms.CharField(label='中文地址', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuchadd2 = forms.CharField(label='中文地址', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuenadd1 = forms.CharField(label='英文地址', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuenadd2 = forms.CharField(label='英文地址', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuenadd3 = forms.CharField(label='英文地址', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cudir = forms.CharField(label='負責人', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cutel = forms.CharField(label='電話號碼', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cufax = forms.CharField(label='傳真號碼', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cupcfax = forms.CharField(label='電腦傳真', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cuattn = forms.CharField(label='聯絡人', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cunminv = forms.CharField(label='發票抬頭', max_length=40, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cusale = forms.CharField(label='業務員', max_length=8, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    custmk = forms.CharField(label='附註', max_length=40, required=False, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    cucgdt = forms.DateTimeField(label='建檔日期', required=False, widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    cucrdt = forms.DateTimeField(label='異動日期', required=False, widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    cutrdt = forms.DateTimeField(label='最後往來日', required=False, widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))


    class Meta:
        model = Custcsn
        fields = '__all__'