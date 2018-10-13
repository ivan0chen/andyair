from django.db import models
from custcsn.models import Custcsn
from main.models import OrgDest
from main.models import WhoColumns


class Mawbin(WhoColumns):
    mawb = models.CharField(max_length=12, unique=True)
    seqnr = models.CharField(max_length=15, blank=True)
    prsdd = models.DateField(blank=True)
    nrhbhold = models.IntegerField(default=0, null=True, blank=True)
    podfax = models.CharField(max_length=1, blank=True)
    agtcode = models.ForeignKey(Custcsn, on_delete=models.SET_NULL, max_length=6, blank=True, null=True)
    mfrom = models.ForeignKey(OrgDest, on_delete=models.SET_NULL, max_length=3, blank=True, null=True)
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
    mcurncy = models.CharField(max_length=3, blank=True)
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
