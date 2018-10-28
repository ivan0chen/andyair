from django import forms
import decimal
from custcsn.models import Custcsn
from shpr.models import Shpr
from custadv.models import Custadv
from main.models import OrgDest
from exrate.models import Exrate
from awbin.models import Mawbin, Hawbin

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

class HawbinForm(forms.ModelForm):
    YN_CHOICES = (('Y', 'Y'), ('N', 'N'))
    hawb = forms.CharField(label='HAWB#', max_length=12, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    hlotnr = forms.CharField(label='LOT#', max_length=9, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    belong = forms.CharField(label='Belong#', max_length=9, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    nrofshb = forms.IntegerField(label='併分單筆數', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'size':'2', 'class': 'form-control input-sm'}))
    pkgofhb = forms.IntegerField(label='件數', min_value=0, max_value=9999, widget=forms.NumberInput(attrs={'size':'4', 'class': 'form-control input-sm'}))
    hseqnr = forms.CharField(label='分號', max_length=4, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    hshpr = forms.ModelChoiceField(label='出貨人', empty_label="請選擇出貨人", queryset=Shpr.objects.all().order_by('csname'),
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    hcnee = forms.ModelChoiceField(label='收貨人', empty_label="請選擇收貨人", queryset=Custcsn.objects.all().order_by('cunmc'),
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    hnotify = forms.ModelChoiceField(label='通知人', empty_label="請選擇通知人", queryset=Custadv.objects.all().order_by('ipntfy'),
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    hfrom = forms.ModelChoiceField(label='起運站', empty_label="選擇起運站", queryset=OrgDest.objects.all().order_by('code'),
                                   widget=forms.Select(attrs={'class':'form-control input-sm'}))
    hrlsdd = forms.DateField(label='贖單日',
                             widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm', 'placeholder':'yyyy-mm-dd hh:ii'}))

    ro = forms.CharField(label='指定貨?', max_length=1, initial='N',
                         widget=forms.Select(choices=YN_CHOICES, attrs={'class': 'form-control input-sm'}))
    hslsman = forms.CharField(label='業務', max_length=2,
                         widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    hacct = forms.CharField(label='月結?', max_length=1, initial='N',
                            widget=forms.Select(choices=YN_CHOICES, attrs={'class': 'form-control input-sm'}))
    trans = forms.CharField(label='押轉否? & D/N', max_length=1, initial='N',
                            widget=forms.Select(choices=YN_CHOICES, attrs={'class': 'form-control input-sm'}))
    fnldest = forms.ModelChoiceField(label='目的地', empty_label="選擇目的地", queryset=OrgDest.objects.all().order_by('code'),
                                   widget=forms.Select(attrs={'class':'form-control input-sm'}))
    trsdb = forms.CharField(label='D/N', max_length=6,
                         widget=forms.TextInput(attrs={'style':'width:100px','class':'form-control input-sm', 'placeholder':'Debit Note'}))
    cusapp = forms.CharField(label='報關否?', max_length=1, initial='N',
                             widget=forms.Select(choices=YN_CHOICES, attrs={'class': 'form-control input-sm'}))
    dtd = forms.CharField(label='到戶否? & D/N', max_length=1, initial='N',
                          widget=forms.Select(choices=YN_CHOICES, attrs={'class': 'form-control input-sm'}))
    dtddb = forms.CharField(label='D/N', max_length=6,
                         widget=forms.TextInput(attrs={'style':'width:100px','class':'form-control input-sm', 'placeholder':'Debit Note'}))
    hgoods = forms.CharField(label='品名', max_length=150,
                         widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    skdpk = forms.CharField(label='合成?', max_length=3, initial='N  ',
                            widget=forms.Select(choices=YN_CHOICES, attrs={'class': 'form-control input-sm'}))
    hpkgnr = forms.IntegerField(label='箱數', min_value=0, max_value=99999, widget=forms.NumberInput(attrs={'size':'5', 'class': 'form-control input-sm'}))
    CHOICES5 = (('CTN', 'CTN'), ('PKG', 'PKG'))
    hpkgunit = forms.CharField(label='單位', max_length=6, initial='CTN',
                               widget=forms.Select(choices=CHOICES5, attrs={'class':'input-sm'}))
    hgw = forms.DecimalField(label='毛重', max_digits=7, decimal_places=1, max_value=999999.9, min_value=0,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    CHOICES6 = (("","單位"),('KGS', 'KGS'), ('LBS', 'LBS'))
    hgwunit = forms.CharField(label='單位', max_length=3, initial='KGS',
                              widget=forms.Select(choices=CHOICES6, attrs={'class':'input-sm'}))
    hchgwt = forms.DecimalField(label='計價重', max_digits=7, decimal_places=1, max_value=999999.9, min_value=0,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 7, 'type': 'number'}))
    hchgunit = forms.CharField(label='單位', max_length=3, initial='KGS',
                              widget=forms.Select(choices=CHOICES6, attrs={'class':'input-sm'}))
    hkgchgwt = forms.DecimalField(label='=(KG) & 運費CP', max_digits=7, decimal_places=1, max_value=999999.9, min_value=0,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm', 'placeholder':'=(KG)'}))
    CHOICES7 = (('CC', 'CC'), ('PP', 'PP'))
    hccpp = forms.CharField(label='運費CP', max_length=2, initial='PP',
                            widget=forms.Select(choices=CHOICES7, attrs={'class': 'input-sm'}))
    hcurncy = forms.ModelChoiceField(label='幣別 & 匯率', empty_label="選擇幣別", queryset=Exrate.objects.all(), to_field_name='code', required=False,
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    hexchg = forms.DecimalField(label='匯率',max_digits=9, decimal_places=5, max_value=9999.99999, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'style':'width:100px', 'readonly':'readonly', 'class':'form-control input-sm',
                                                                'placeholder':'匯率'}))
    hfrtrte = forms.DecimalField(label='單價 & 運費', max_digits=6, decimal_places=2, max_value=9999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm', 'placeholder':'單價'}))
    hwtchrg =forms.DecimalField(label='運費', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'style':'width:100px', 'readonly':'readonly', 'class':'form-control input-sm',
                                                                'placeholder':'運費'}))
    hduagt = forms.DecimalField(label='DUAGT', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    httlfrt = forms.DecimalField(label='總運費', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    htlfrtwd = forms.DecimalField(label='=TWD', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))

    vwdspct = forms.DecimalField(label='體積差折讓%', max_digits=4, decimal_places=2, max_value=99.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 6, 'type': 'number'}))
    vwdskglb = forms.DecimalField(label='總折', max_digits=6, decimal_places=2, max_value=9999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 8, 'type': 'number'}))
    vwdsper = forms.CharField(label='PER', max_length=2,
                                widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    ttldsamt = forms.DecimalField(label='金額', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    ttldstwd = forms.DecimalField(label='=TWD', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    hflfrtwd = forms.DecimalField(label='應收TWD', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    hpayby = forms.CharField(label='付費方式', max_length=1, initial='K',
                             widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    howe = forms.IntegerField(label='尚欠', min_value=0, max_value=99999,
                              widget=forms.NumberInput(attrs={'size':'5', 'class': 'form-control input-sm'}))
    hadvsdd = forms.DateField(label='通知日期',
                             widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm datepicker'}))
    sccurn =  forms.ModelChoiceField(label='S/C => 幣別 & %', empty_label="選擇幣別", queryset=Exrate.objects.all(), to_field_name='code', required=False,
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    scpct = forms.DecimalField(label='SC%', max_digits=4, decimal_places=2, max_value=99.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'style':'width:100px', 'class':'form-control input-sm','placeholder':'%'}))
    scpkls = forms.DecimalField(label='PKLS & PER', max_digits=6, decimal_places=2, max_value=9999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control input-sm','maxlength': 8, 'type': 'number'}))
    scper = forms.CharField(label='SCPER', max_length=2,
                                widget=forms.TextInput(attrs={'style':'width:100px', 'class':'form-control input-sm','placeholder':'PER'}))
    scamt = forms.DecimalField(label='小計', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    scamtwd = forms.DecimalField(label='計台幣', max_digits=8, decimal_places=2, max_value=999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 8, 'type': 'number'}))
    sctowho = forms.CharField(label='TO', max_length=12,
                                widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    codcurn = forms.ModelChoiceField(label='COD => 幣別', empty_label="選擇幣別", queryset=Exrate.objects.all(), to_field_name='code', required=False,
                                     widget=forms.Select(attrs={'class':'form-control input-sm'}))
    codamt = forms.DecimalField(label='COD金額', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))
    codrcvdd = forms.DateField(label='收訖日',
                             widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm datepicker'}))
    codpaydd = forms.DateField(label='付給日',
                             widget=forms.TextInput(attrs={'readonly':'readonly','class':'form-control input-sm datepicker'}))
    hrmk = forms.CharField(label='附記', max_length=1,
                                widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    hdb = forms.CharField(label='是否完整收到=> RCVD D/N (CC ONLY)', max_length=1, initial='P',
                             widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    hcd = forms.CharField(label='RCVD C/N(針對指定貨)', max_length=1, initial='P',
                             widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    httlamt = forms.DecimalField(label='總應收', max_digits=9, decimal_places=2, max_value=9999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    ttlocamt = forms.DecimalField(label='ttlocamt', max_digits=9, decimal_places=2, max_value=9999999.99, min_value=0, required=False,
                                widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    # dbcurn = forms.ModelChoiceField(label='DB幣別', empty_label="選擇幣別", queryset=Exrate.objects.all(), to_field_name='code', required=False,
    #                                  widget=forms.Select(attrs={'class':'form-control input-sm'}))
    # dbexrate = forms.DecimalField(label='DB匯率',max_digits=9, decimal_places=5, max_value=9999.99999, min_value=0, required=False,
    #                             widget=forms.NumberInput(attrs={'style':'width:100px', 'readonly':'readonly', 'class':'form-control input-sm','maxlength': 9, 'type': 'number'}))
    # dbamount = forms.DecimalField(label='dbamount', max_digits=10, decimal_places=2, max_value=99999999.99, min_value=0, required=False,
    #                             widget=forms.NumberInput(attrs={'readonly':'readonly', 'class':'form-control input-sm','maxlength': 10, 'type': 'number'}))

    class Meta:
        model = Hawbin
        exclude = ['mawb',]