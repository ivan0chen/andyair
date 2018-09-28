from django.db import models
from main.models import WhoColumns

class Invpars(WhoColumns):
    midno = models.CharField(max_length=8, unique=True)
    mname = models.CharField(max_length=52)
    taxno = models.CharField(max_length=9)
    seqyy = models.IntegerField(default=0, null=True, blank=True)
    seq01 = models.IntegerField(default=0, null=True, blank=True)
    seq02 = models.IntegerField(default=0, null=True, blank=True)
    seq03 = models.IntegerField(default=0, null=True, blank=True)
    seq04 = models.IntegerField(default=0, null=True, blank=True)
    seq05 = models.IntegerField(default=0, null=True, blank=True)
    seq06 = models.IntegerField(default=0, null=True, blank=True)
    seq07 = models.IntegerField(default=0, null=True, blank=True)
    seq08 = models.IntegerField(default=0, null=True, blank=True)
    seq09 = models.IntegerField(default=0, null=True, blank=True)
    seq10 = models.IntegerField(default=0, null=True, blank=True)
    seq11 = models.IntegerField(default=0, null=True, blank=True)
    seq12 = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.mname + '-' + self.midno + '-' + self.taxno

class Invstk(WhoColumns):
    invpars = models.ForeignKey(Invpars, on_delete=models.CASCADE)
    invyymm = models.CharField(max_length=7, unique=True)
    invchar = models.CharField(max_length=2)
    sttno = models.IntegerField(default=0, null=True, blank=True)
    endno = models.IntegerField(default=0, null=True, blank=True)
    nowno = models.IntegerField(default=0, null=True, blank=True)
    usedd = models.DateField(blank=True, null=True)
    boxno = models.CharField(max_length=2, blank=True, null=True)
    machno = models.CharField(max_length=1,  blank=True, null=True)

    def __str__(self):
        return self.invyymm + '-' + self.invchar + '-' + str(self.sttno) + '-' + str(self.endno)


