from django import forms
from shpr.models import Shpr

class ShprForm(forms.ModelForm):
    cscode = forms.CharField(label='Client Code', min_length=7, max_length=10, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    CHOICES = (('1','111'),('2','222'),('3','333'))
    kind = forms.CharField(label='Kind', max_length=1, required=True, widget=forms.Select(choices=CHOICES, attrs={'class':'form-control'}))
    csname = forms.CharField(label='Title', max_length=40, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address', max_length=120, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    tel1 = forms.CharField(label='Telephone1', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    tel2 = forms.CharField(label='Telephone2', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    fax1 = forms.CharField(label='Fax1', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    fax2 = forms.CharField(label='Fax2', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    tlx = forms.CharField(label='Telex', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    attn = forms.CharField(label='Attn', max_length=30, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    dest = forms.CharField(label='Origin', max_length=3, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    shipno = forms.CharField(label='Shipno', max_length=7, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    remark = forms.CharField(label='Remark', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Shpr
        fields = '__all__'