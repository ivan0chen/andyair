from django import forms
from awbin.models import Mawbin

class MawbinForm(forms.ModelForm):
    mawb = forms.CharField(label='主提單', max_length=12, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    seqnr = forms.CharField(label='總LOT號', max_length=15, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    prsdd = forms.DateField(label='日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    nrhbhold = forms.IntegerField(label='POD', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    podfax = forms.CharField(label='FAX', max_length=1, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    agtcode = forms.CharField(label='AGENT', max_length=6, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mfrom = forms.CharField(label='起運站', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mdepdd = forms.DateField(label='起飛日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    metaflt = forms.CharField(label='預定班機', max_length=7, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    metadd = forms.DateField(label='', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    marvflt = forms.CharField(label='到達班機', max_length=7, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    marvdd = forms.DateField(label='', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    mpuawbdd = forms.DateField(label='領單日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    mcusdept = forms.CharField(label='受理關別', max_length=2, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    msvcknd = forms.CharField(label='SVCKND', max_length=1, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    marvapt = forms.CharField(label='到達機場', max_length=5, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    munlodwh = forms.CharField(label='卸貨棧', max_length=6, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    nrofhawb = forms.IntegerField(label='分提單筆數', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    mpkgnr = forms.IntegerField(label='箱數', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    mpkgunit = forms.CharField(label='', max_length=6, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mgw = forms.DecimalField(label='毛重', max_digits=7, decimal_places=1, max_value=999999.9,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    mgwunit = forms.CharField(label='', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mchgwt = forms.DecimalField(label='計價重', max_digits=7, decimal_places=1, max_value=999999.9,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    mchgunit = forms.CharField(label='', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mkgchgwt = forms.DecimalField(label='=(KG)', max_digits=7, decimal_places=1, max_value=999999.9,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    mccpp = forms.CharField(label='運費CP', max_length=2, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mcurncy = forms.CharField(label='幣別', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mexchg = forms.DecimalField(label='匯率', max_digits=9, decimal_places=5, max_value=9999.99999,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    mfrtrte = forms.DecimalField(label='單價', max_digits=6, decimal_places=2, max_value=9999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 6, 'type': 'number'}))
    mwtchrg = forms.DecimalField(label='運費', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    mwtchtwd = forms.DecimalField(label='=TWD', max_digits=9, decimal_places=2, max_value=9999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    mduagt = forms.DecimalField(label='DUE AG', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    mducar = forms.DecimalField(label='DUE CA', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    mttlfrt = forms.DecimalField(label='總運費', max_digits=11, decimal_places=2, max_value=999999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 11, 'type': 'number'}))
    mtlfrtwd = forms.DecimalField(label='=TWD', max_digits=9, decimal_places=2, max_value=9999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    rdbnr = forms.IntegerField(label='FULL SETS RECEIVED D/B?', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    rcdnr = forms.IntegerField(label='C/D?', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    trsdbnr = forms.IntegerField(label=' TRANS DB ISSUD?', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    dtddbnr = forms.IntegerField(label='DTD SVC DB ISSUD?', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))

    class Meta:
        model = Mawbin
        fields = '__all__'