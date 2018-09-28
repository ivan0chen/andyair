from django import forms
from invpars.models import Invpars, Invstk

class InvparsForm(forms.ModelForm):
    midno = forms.CharField(label='統一編號', min_length=8, max_length=8,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    mname = forms.CharField(label='營業人名稱', max_length=52,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    taxno = forms.CharField(label='稅籍編號', max_length=9,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    seqyy = forms.IntegerField(label='年發票序號', min_value=0, max_value=999999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq01 = forms.IntegerField(label='01', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq02 = forms.IntegerField(label='02', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq03 = forms.IntegerField(label='03', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq04 = forms.IntegerField(label='04', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq05 = forms.IntegerField(label='05', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq06 = forms.IntegerField(label='06', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq07 = forms.IntegerField(label='07', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq08 = forms.IntegerField(label='08', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq09 = forms.IntegerField(label='09', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq10 = forms.IntegerField(label='10', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq11 = forms.IntegerField(label='11', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))
    seq12 = forms.IntegerField(label='12', min_value=0, max_value=99999,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}))

    class Meta:
        model = Invpars
        fields = '__all__'

class InvstkForm(forms.ModelForm):
    invyymm = forms.CharField(label='年/月', max_length=7,
                              widget=forms.TextInput(attrs={'class':'tabledit-input form-control input-sm'}))
    invchar = forms.CharField(label='字軌', max_length=2,
                              widget=forms.TextInput(attrs={'class':'tabledit-input form-control input-sm'}))
    sttno = forms.IntegerField(label='起始號碼', min_value=0, max_value=99999999,
                                widget=forms.NumberInput(attrs={'class': 'tabledit-input form-control input-sm', 'maxlength': 8, 'type': 'number'}))
    endno = forms.IntegerField(label='訖止號碼', min_value=0, max_value=99999999,
                                widget=forms.NumberInput(attrs={'class': 'tabledit-input form-control input-sm', 'maxlength': 8, 'type': 'number'}))
    nowno = forms.IntegerField(label='目前使用', min_value=0, max_value=99999999, required=False,
                                widget=forms.NumberInput(attrs={'class': 'tabledit-input form-control input-sm', 'maxlength': 8, 'type': 'number'}))
    usedd = forms.DateField(label='使用日期', required=False,
                            widget=forms.TextInput(attrs={'readonly':'readonly','class':'tabledit-input form-control input-sm'}))
    boxno = forms.CharField(label='盒號', max_length=2, required=False,
                            widget=forms.TextInput(attrs={'class': 'tabledit-input form-control input-sm'}))
    machno = forms.CharField(label='機器', max_length=1, required=False,
                             widget=forms.TextInput(attrs={'class': 'tabledit-input form-control input-sm'}))

    class Meta:
        model = Invstk
        exclude = ('invpars',)
