from django.db import models
from custcsn.models import Custcsn
from custadv.models import Custadv
from shpr.models import Shpr
from main.models import OrgDest
# from inpfee.models import Inpfee
# from exrate.models import Exrate
from main.models import WhoColumns


class Mawbin(WhoColumns):
    mawb = models.CharField(max_length=12, unique=True)
    seqnr = models.CharField(max_length=15, blank=True)
    prsdd = models.DateField(blank=True)
    nrhbhold = models.IntegerField(default=0, null=True, blank=True)
    podfax = models.CharField(max_length=1, blank=True)
    agtcode = models.ForeignKey(Custcsn, on_delete=models.DO_NOTHING, max_length=6, blank=True, null=True)
    mfrom = models.ForeignKey(OrgDest, on_delete=models.DO_NOTHING, max_length=3, blank=True, null=True)
    mdepdd = models.DateField(blank=True)
    metaflt = models.CharField(max_length=7, blank=True)
    metadd = models.DateField(blank=True)
    marvflt = models.CharField(max_length=7, blank=True)
    marvdd = models.DateField(blank=True)
    mpuawbdd = models.DateField(blank=True)
    mcusdept = models.CharField(max_length=2, blank=True)
    msvcknd = models.CharField(max_length=1, blank=True)
    marvapt = models.CharField(max_length=5, blank=True)
    munlodwh = models.CharField(max_length=6, blank=True)
    nrofhawb = models.IntegerField(default=0, null=True, blank=True)
    mpkgnr = models.IntegerField(default=0, null=True, blank=True)
    mpkgunit = models.CharField(max_length=6, blank=True)
    mgw = models.DecimalField(max_digits=7, decimal_places=1, null=True,blank=True)
    mgwunit = models.CharField(max_length=3, blank=True)
    mchgwt = models.DecimalField(max_digits=7, decimal_places=1, null=True,blank=True)
    mchgunit = models.CharField(max_length=3, blank=True)
    mkgchgwt = models.DecimalField(max_digits=7, decimal_places=1, null=True,blank=True)
    mccpp = models.CharField(max_length=2, blank=True)
    mcurncy = models.CharField(max_length=3, blank=True, null=True)
    mexchg = models.DecimalField(max_digits=9, decimal_places=5, null=True,blank=True)
    mfrtrte = models.DecimalField(max_digits=6, decimal_places=2, null=True,blank=True)
    mwtchrg = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    mwtchtwd = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    mduagt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    mducar = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    mttlfrt = models.DecimalField(max_digits=11, decimal_places=2, null=True,blank=True)
    mtlfrtwd = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    rdbnr = models.IntegerField(default=0, null=True, blank=True)
    rcdnr = models.IntegerField(default=0, null=True, blank=True)
    trsdbnr = models.IntegerField(default=0, null=True, blank=True)
    dtddbnr = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.mawb + '-' + self.seqnr

class Hawbin(WhoColumns):
    mawb = models.ForeignKey(Mawbin, on_delete=models.CASCADE)
    hawb = models.CharField(max_length=12)
    hlotnr = models.CharField(max_length=9, blank=True)
    belong = models.CharField(max_length=9, blank=True)
    nrofshb = models.IntegerField(default=0, null=True, blank=True)
    pkgofhb = models.IntegerField(default=0, null=True, blank=True)
    hseqnr = models.CharField(max_length=4, blank=True)
    hshpr = models.ForeignKey(Shpr, on_delete=models.DO_NOTHING, max_length=6, blank=True, null=True)
    hcnee = models.ForeignKey(Custcsn, on_delete=models.DO_NOTHING, max_length=6, blank=True, null=True)
    hnotify = models.ForeignKey(Custadv, on_delete=models.DO_NOTHING, max_length=6, blank=True, null=True)
    hfrom = models.ForeignKey(OrgDest, on_delete=models.DO_NOTHING, max_length=3, blank=True, null=True)
    hrlsdd = models.DateTimeField(blank=True)
    # hrlstm = models.TimeField(blank=True)
    ro = models.CharField(max_length=1, default="N", blank=True)
    hslsman = models.CharField(max_length=2, blank=True)
    hacct = models.CharField(max_length=1, default="N", blank=True)
    trans = models.CharField(max_length=1, default="N", blank=True)
    fnldest = models.CharField(max_length=3, blank=True)
    trsdb = models.CharField(max_length=6, blank=True)
    cusapp = models.CharField(max_length=1, default="N", blank=True)
    dtd = models.CharField(max_length=1, default="N", blank=True)
    dtddb = models.CharField(max_length=6, blank=True)
    hgoods = models.CharField(max_length=150, blank=True)
    skdpk = models.CharField(max_length=3, default="N  ", blank=True)
    hpkgnr = models.IntegerField(default=0, null=True, blank=True)
    hpkgunit = models.CharField(max_length=3, default="CTN", blank=True)
    hgw = models.DecimalField(max_digits=7, decimal_places=1, null=True,blank=True)
    hgwunit = models.CharField(max_length=3, default="KGS", blank=True)
    hchgwt = models.DecimalField(max_digits=7, decimal_places=1, null=True,blank=True)
    hchgunit = models.CharField(max_length=3, default="KGS", blank=True)
    hkgchgwt = models.DecimalField(max_digits=7, decimal_places=1, null=True,blank=True)
    hccpp = models.CharField(max_length=2, default="PP", blank=True)
    hcurncy = models.CharField(max_length=3, blank=True, null=True)
    hexchg = models.DecimalField(max_digits=9, decimal_places=5, null=True,blank=True)
    hfrtrte = models.DecimalField(max_digits=6, decimal_places=2, null=True,blank=True)
    hwtchrg = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    hduagt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    httlfrt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    htlfrtwd = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    vwdspct = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True)
    vwdskglb = models.DecimalField(max_digits=6, decimal_places=2, null=True,blank=True)
    vwdsper = models.CharField(max_length=2, blank=True)
    ttldsamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    ttldstwd = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    hflfrtwd = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    hpayby = models.CharField(max_length=1, default="K", blank=True)
    howe = models.IntegerField(default=0, null=True, blank=True)
    hadvsdd = models.DateField(blank=True)
    sccurn =  models.CharField(max_length=3, blank=True, null=True)
    scpct = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True)
    scpkls = models.DecimalField(max_digits=6, decimal_places=2, null=True,blank=True)
    scper = models.CharField(max_length=2, blank=True, null=True)
    scamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    scamtwd = models.DecimalField(max_digits=8, decimal_places=2, null=True,blank=True)
    sctowho = models.CharField(max_length=12, blank=True, null=True)
    codcurn = models.CharField(max_length=3, blank=True, null=True)
    codamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    codrcvdd = models.DateField(blank=True)
    codpaydd = models.DateField(blank=True)
    hrmk = models.CharField(max_length=1, blank=True, null=True)
    hdb = models.CharField(max_length=1, default="P", blank=True)
    hcd = models.CharField(max_length=1, default="P", blank=True)
    httlamt = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    ttlocamt = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    # dbcurn = models.CharField(max_length=3, blank=True, null=True)
    # dbexrate = models.DecimalField(max_digits=9, decimal_places=5, null=True,blank=True)
    # dbamount = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)

    class Meta:
        unique_together = (('mawb', 'hawb'),)

    def __str__(self):
        return self.hawb + '-' + self.hlotnr

class Acctin(WhoColumns):
    mawb = models.ForeignKey(Mawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    hawb = models.ForeignKey(Hawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    dc = models.CharField(max_length=1, blank=True, null=True)
    dcno = models.CharField(max_length=9, unique=True)
    dccurn = models.CharField(max_length=3, blank=True, null=True)
    exrate1 = models.DecimalField(max_digits=9, decimal_places=5, null=True,blank=True)
    dcamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    issdd = models.DateField(null=True,blank=True)
    status0 = models.CharField(max_length=1, blank=True, null=True)
    status1 = models.CharField(max_length=1, blank=True, null=True)
    status2 = models.CharField(max_length=1, blank=True, null=True)
    status3 = models.CharField(max_length=1, blank=True, null=True)
    rcvdd = models.DateField(null=True,blank=True)
    rcvamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    balamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    payclr = models.CharField(max_length=1, blank=True, null=True)
    actagno1 = models.ForeignKey(Custcsn, on_delete=models.DO_NOTHING, max_length=6, blank=True, null=True)

    def __str__(self):
        return  self.dcno + ' - ' + str(self.dcamt)

class Rmkin(WhoColumns):
    mawb = models.ForeignKey(Mawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    hawb = models.ForeignKey(Hawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    codr = models.CharField(max_length=3)
    statement = models.CharField(max_length=60)
    irrno = models.CharField(max_length=2)

    def __str__(self):
        return  self.codr + ' - ' + self.statement

class Accin(WhoColumns):
    mawb = models.ForeignKey(Mawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    hawb = models.ForeignKey(Hawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    accno = models.CharField(max_length=10, unique=True)
    cscode = models.ForeignKey(Custcsn, on_delete=models.DO_NOTHING, max_length=6, blank=True, null=True)
    invidno = models.CharField(max_length=10)
    accdate = models.DateField(blank=True)
    accamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    ttltax = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    recamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    balamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    invno = models.CharField(max_length=11, null=True,blank=True)
    dpt = models.CharField(max_length=1, null=True,blank=True)
    mth = models.CharField(max_length=1, null=True,blank=True)
    appdate = models.DateField(blank=True, null=True)
    invno2 = models.CharField(max_length=11, null=True,blank=True)

    def __str__(self):
        return self.accno + '-' + str(self.accamt) + '-' + str(self.ttltax)

class Accdtl(WhoColumns):
    mawb = models.ForeignKey(Mawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    hawb = models.ForeignKey(Hawbin, on_delete=models.DO_NOTHING, blank=True, null=True)
    accno = models.CharField(max_length=10, unique=True)
    codo = models.CharField(max_length=3)
    ocname = models.CharField(max_length=30)
    tax = models.CharField(max_length=1)
    ocamt = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    occost = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)

    def __str__(self):
        return self.accno + '-' + self.codo + '-' + str(self.ocamt)

