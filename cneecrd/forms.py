from django import forms
from cneecrd.models import Cneecrd
from django.contrib import messages

class CneecrdForm(forms.ModelForm):
    # custcsn = forms.CharField(label='客戶代碼', widget=forms.Select(attrs={'class':'form-control'}))
    crdamt = forms.DecimalField(label='信用額度（總）', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control','maxlength': 10, 'type': 'number',}))
    aro = forms.DecimalField(label='出口應收', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ars = forms.DecimalField(label='進口發單應收', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    arc = forms.DecimalField(label='進口報關應收', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    arcod = forms.IntegerField(label='COD', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control'}))

    class Meta:
        model = Cneecrd
        exclude = ('custcsn',)

    # def clean(self):
    #     cleaned_data = super(CneecrdForm, self).clean()
    #     print(cleaned_data)
    #     crdamt = cleaned_data.get('crdamt')
    #     aro = cleaned_data.get('aro')
    #     ars = cleaned_data.get('ars')
    #     arc = cleaned_data.get('arc')
    #     # print(aro)
    #     # print(type(aro))
    #     # print(float(crdamt))
    #     # print(float(aro)+float(ars)+float(arc))
    #     # print(float(crdamt) < (float(aro)+float(ars)+float(arc)))
    #     if float(crdamt) < (float(aro)+float(ars)+float(arc)):
    #         raise forms.ValidationError('輸入錯誤！ 信用額度（總）< 出口應收+進口發單應收+進口報關應收')
    #     return cleaned_data


