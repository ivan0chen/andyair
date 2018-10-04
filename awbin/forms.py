from django import forms
from awbin.models import Mawbin

class MawbinForm(forms.ModelForm):
    mawb = models.CharField(label='主提單', max_length=12, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    seqnr = models.CharField(label='總LOT號', max_length=15, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    prsdd = models.DateField(label='日期', blank=True, widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    nrhbhold = models.IntegerField(label='POD', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    podfax = models.CharField(label='FAX', max_length=1, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    agtcode = models.CharField(label='AGENT', max_length=6, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mfrom = models.CharField(label='起運站', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mdepdd = models.DateField(label='起飛日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    metaflt = models.CharField(label='預定班機', max_length=7, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    metadd = models.DateField(label='', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    marvflt = models.CharField(label='到達班機', max_length=7, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    marvdd = models.DateField(label='', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    mpuawbdd = models.DateField(label='領單日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm'}))
    mcusdept = models.CharField(label='受理關別', max_length=2, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    msvcknd = models.CharField(label='SVCKND', max_length=1, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    marvapt = models.CharField(label='到達機場', max_length=5, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    munlodwh = models.CharField(label='卸貨棧', max_length=6, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    nrofhawb = models.IntegerField(label='分提單筆數', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    mpkgnr = models.IntegerField(label='箱數', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    mpkgunit = models.CharField(label='', max_length=6, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mgw = models.DecimalField(label='毛重', max_digits=7, decimal_places=1, max_value=999999.9,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number',}))
    mgwunit = models.CharField(label='', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mchgwt = models.DecimalField(label='計價重', max_digits=7, decimal_places=1, max_value=999999.9,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number',}))
    mchgunit = models.CharField(label='', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mkgchgwt = models.DecimalField(label='=(KG)', max_digits=7, decimal_places=1, max_value=999999.9,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number',}))
    mccpp = models.CharField(label='運費CP', max_length=2, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mcurncy = models.CharField(label='幣別', max_length=3, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    mexchg = models.DecimalField(label='匯率', max_digits=9, decimal_places=5, max_value=9999.99999,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 9, 'type': 'number',}))
    mfrtrte = models.DecimalField(label='單價', max_digits=6, decimal_places=2, max_value=9999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 6, 'type': 'number',}))
    mwtchrg = models.DecimalField(label='運費', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number',}))
    mwtchtwd = models.DecimalField(label='=TWD', max_digits=9, decimal_places=2, max_value=9999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 9, 'type': 'number',}))
    mduagt = models.DecimalField(label='DUE AG', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number',}))
    mducar = models.DecimalField(label='DUE CA', max_digits=10, decimal_places=2, max_value=99999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number',}))
    mttlfrt = models.DecimalField(label='總運費', max_digits=11, decimal_places=2, max_value=999999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 11, 'type': 'number',}))
    mtlfrtwd = models.DecimalField(label='=TWD', max_digits=9, decimal_places=2, max_value=9999999.99,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 9, 'type': 'number',}))
    rdbnr = models.IntegerField(label='FULL SETS RECEIVED D/B?', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    rcdnr = models.IntegerField(label='C/D?', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    trsdbnr = models.IntegerField(label=' TRANS DB ISSUD?', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    dtddbnr = models.IntegerField(label='DTD SVC DB ISSUD?', default=0, min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))

    def __str__(self):
        return self.mawb + '-' + self.seqnr