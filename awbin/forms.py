from django import forms
import decimal
from custcsn.models import Custcsn
from main.models import OrgDest
from exrate.models import Exrate
from awbin.models import Mawbin

class MawbinForm(forms.ModelForm):
    mawb = forms.CharField(label='主提單', max_length=12, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    seqnr = forms.CharField(label='總LOT號', max_length=15, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    prsdd = forms.DateField(label='日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm datepicker'}))
    nrhbhold = forms.IntegerField(label='POD', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    podfax = forms.CharField(label='FAX', max_length=1, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    agtcode = forms.ModelChoiceField(label='AGENT', empty_label="Choose a Agent", queryset=Custcsn.objects.all().order_by('cunme'),
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    mfrom = forms.ModelChoiceField(label='起運站', empty_label="選擇起運站", queryset=OrgDest.objects.all().order_by('code'),
                                   widget=forms.Select(attrs={'class':'form-control input-sm'}))
    mdepdd = forms.DateField(label='起飛日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm datepicker'}))
    metaflt = forms.CharField(label='預定班機', max_length=7, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    metadd = forms.DateField(label='預定日期', widget=forms.TextInput(attrs={'style':'width:150px','readonly':'readonly','class':'form-control input-sm datepicker'}))
    marvflt = forms.CharField(label='到達班機', max_length=7, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    marvdd = forms.DateField(label='到達日期', widget=forms.TextInput(attrs={'style':'width:150px','readonly':'readonly','class':'form-control input-sm datepicker'}))
    mpuawbdd = forms.DateField(label='領單日期', widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm datepicker'}))
    CHOICES1 = (('CA', '台北關'), ('BF', '高雄關'))
    mcusdept = forms.CharField(label='受理關別', max_length=2, widget=forms.Select(choices=CHOICES1, attrs={'class':'form-control input-sm'}))
    CHOICES2 = (('1', '直走單'), ('2', '非直走單'),('3','併裝莊主'),('4','併裝莊友'),('9','向同行領單'))
    msvcknd = forms.CharField(label='SVCKND', max_length=1, widget=forms.Select(choices=CHOICES2, attrs={'class':'form-control input-sm'}))
    CHOICES3 = (('TWTPE', '台北機場'), ('TWKHH', '高雄機場'))
    marvapt = forms.CharField(label='到達機場', max_length=5, widget=forms.Select(choices=CHOICES3, attrs={'class':'form-control input-sm'}))
    CHOICES4 = (('C2001', '台北貨運站'), ('C2007', '永儲'), ('C2009', '遠翔'), ('B2140', '高雄貨運站'))
    munlodwh = forms.CharField(label='卸貨棧', max_length=6, widget=forms.Select(choices=CHOICES4, attrs={'class':'form-control input-sm'}))
    nrofhawb = forms.IntegerField(label='分提單筆數', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    mpkgnr = forms.IntegerField(label='箱數', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    CHOICES5 = (('CTN', 'CTN'), ('PKG', 'PKG'))
    mpkgunit = forms.CharField(label='單位', max_length=6, widget=forms.Select(choices=CHOICES5, attrs={'class':'input-sm'}))
    mgw = forms.DecimalField(label='毛重', max_digits=7, decimal_places=1, max_value=999999.9, min_value=0,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    CHOICES6 = (("","單位"),('KGS', 'KGS'), ('LBS', 'LBS'))
    mgwunit = forms.CharField(label='單位', max_length=3, widget=forms.Select(choices=CHOICES6, attrs={'class':'input-sm'}))
    mchgwt = forms.DecimalField(label='計價重', max_digits=7, decimal_places=1, max_value=999999.9, min_value=0,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    mchgunit = forms.CharField(label='單位', max_length=3, widget=forms.Select(choices=CHOICES6, attrs={'class':'input-sm'}))
    mkgchgwt = forms.DecimalField(label='=(KG) & 運費CP', max_digits=7, decimal_places=1, max_value=999999.9, min_value=0,
                                widget=forms.NumberInput(attrs={'readonly':'readonly','class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    CHOICES7 = (('CC', 'CC'), ('PP', 'PP'))
    mccpp = forms.CharField(label='運費CP', max_length=2, widget=forms.Select(choices=CHOICES7, attrs={'class':'input-sm'}))

    mcurncy = forms.ModelChoiceField(label='幣別 & 匯率', empty_label="選擇幣別", queryset=Exrate.objects.all(), to_field_name='code', required=False,
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))

    mexchg = forms.DecimalField(label='匯率',max_digits=9, decimal_places=5, max_value=9999.99999, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'style':'width:100px', 'readonly':'readonly', 'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    mfrtrte = forms.DecimalField(label='單價', max_digits=6, decimal_places=2, max_value=9999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 6, 'type': 'number'}))
    mwtchrg = forms.DecimalField(label='運費', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    mwtchtwd = forms.DecimalField(label='=TWD', max_digits=9, decimal_places=2, max_value=9999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    mduagt = forms.DecimalField(label='DUE AG', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    mducar = forms.DecimalField(label='DUE CA', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    mttlfrt = forms.DecimalField(label='總運費', max_digits=11, decimal_places=2, max_value=999999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 11, 'type': 'number'}))
    mtlfrtwd = forms.DecimalField(label='=TWD', max_digits=9, decimal_places=2, max_value=9999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    rdbnr = forms.IntegerField(label='FULL SETS RECEIVED D/B?', min_value=0, max_value=99, required=False,
                               widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    rcdnr = forms.IntegerField(label='C/D?', min_value=0, max_value=99, required=False,
                               widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    trsdbnr = forms.IntegerField(label=' TRANS DB ISSUD?', min_value=0, max_value=99, required=False,
                                 widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    dtddbnr = forms.IntegerField(label='DTD SVC DB ISSUD?', min_value=0, max_value=99, required=False,
                                 widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))

    class Meta:
        model = Mawbin
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(MawbinForm, self).__init__(*args, **kwargs)
    #     # assign a (computed) default value to the choice field
    #     self.fields['mcurncy'].queryset = Exrate.objects.all()
    #     self.fields['mcurncy'].initial = lambda obj: "%s" % (obj.code)
    #     # self.fields['mcurncy'].label_from_instance = lambda obj: "%s : %s" % (obj.code, obj.ex_orate)
    #     # self.fields['mexchg'].initial = lambda obj: obj.ex_orate

    def clean_mcurncy(self):
        m_mcurncy = self.cleaned_data['mcurncy'].code
        # print('mcurncy',m_mcurncy)
        return m_mcurncy

    def clean_mkgchgwt(self):

        cleaned_data = super(MawbinForm, self).clean()
        mgwunit = cleaned_data.get('mgwunit')
        mchgunit = cleaned_data.get('mchgunit')
        mgw = cleaned_data.get('mgw')
        mchgwt = cleaned_data.get('mchgwt')
        mkgchgwt = cleaned_data.get('mkgchgwt')
        # print('mgwunit',mgwunit)
        # print('mgw',mgw)
        # print('mchgwt',mchgwt)
        # print('mchgunit',mchgunit)
        # print('mkgchgwt',mkgchgwt)
        chgwt_check = True
        if mgwunit == mchgunit:
            if mchgwt < mgw:
                chgwt_check = False
        else:
            if (mgwunit == "LBS"):
                if (mchgwt < (mgw / decimal.Decimal.from_float(2.2046))):
                    chgwt_check = False
            else:
                if (mkgchgwt < mgw):
                    chgwt_check = False
        if not chgwt_check:
            raise forms.ValidationError("計價重不得小於毛重!!")

        return mchgwt