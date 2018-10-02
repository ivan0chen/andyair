from django import forms
from inpfee.models import Inpfee

class InpfeeForm(forms.ModelForm):
    code = forms.CharField(label='代碼', min_length=3, max_length=3, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label='費用名稱', max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    CHOICES = (('Y', '是'), ('N', '否'))
    tax =   forms.CharField(label='TAX', max_length=1, required=True, widget=forms.Select(choices=CHOICES, attrs={'class':'form-control'}))
    ocamt = forms.DecimalField(label='金額', max_digits=9, decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Inpfee
        fields = '__all__'