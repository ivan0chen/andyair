from django import forms
from exrate.models import Exrate

class ExrateForm(forms.ModelForm):
    code = forms.CharField(label='CODE', min_length=3, max_length=3, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    currency = forms.CharField(label='外幣名稱', max_length=25, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    ex_irate = forms.DecimalField(label='買入', max_digits=9, decimal_places=5, widget=forms.NumberInput(attrs={'class':'form-control'}))
    ex_orate = forms.DecimalField(label='賣出', max_digits=9, decimal_places=5, widget=forms.NumberInput(attrs={'class':'form-control'}))
    lastdate = forms.DateField(label='日期', required=False,
                               widget=forms.TextInput(attrs={'readonly': 'readonly', 'class':'form-control'}))

    class Meta:
        model = Exrate
        fields = '__all__'