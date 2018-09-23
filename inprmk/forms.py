from django import forms
from inprmk.models import Inprmk

class InprmkForm(forms.ModelForm):
    code = forms.CharField(label='代碼', min_length=3, max_length=3, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label='備註說明', max_length=60, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Inprmk
        fields = '__all__'