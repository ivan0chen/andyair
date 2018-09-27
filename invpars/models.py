from django.db import models
from main.models import WhoColumns

class Invpars(WhoColumns):
    midno = models.CharField(max_length=8, unique=True)
    mname = models.CharField(max_length=52)
    taxno = models.CharField(max_length=9)
    seqyy = models.IntegerField(max_length=6)
    seq01 = models.IntegerField(max_length=5)
    seq02 = models.IntegerField(max_length=5)
    seq03 = models.IntegerField(max_length=5)
    seq04 = models.IntegerField(max_length=5)
    seq05 = models.IntegerField(max_length=5)
    seq06 = models.IntegerField(max_length=5)
    seq07 = models.IntegerField(max_length=5)
    seq08 = models.IntegerField(max_length=5)
    seq09 = models.IntegerField(max_length=5)
    seq10 = models.IntegerField(max_length=5)
    seq11 = models.IntegerField(max_length=5)
    seq12 = models.IntegerField(max_length=5)


    def __str__(self):
        return self.mname + '-' + self.midno + '-' + self.taxno

class Invstk(WhoColumns):
    invpars = models.ForeignKey(Invpars, on_delete=models.CASCADE)
    invyymm = models.CharField(max_length=7, unique=True)
    invchar = models.CharField(max_length=2)
    sttno = models.IntegerField(max_length=8)
    endno = models.IntegerField(max_length=8)
    nowno = models.IntegerField(max_length=8, blank=True, null=True)
    usedd = models.DateField(blank=True, null=True)
    boxno = models.CharField(max_length=2, blank=True, null=True)
    machno = models.CharField(max_length=1,  blank=True, null=True)

    def __str__(self):
        return self.invyymm + '-' + self.invchar + '-' + str(self.sttno) + '-' + str(self.endno)


