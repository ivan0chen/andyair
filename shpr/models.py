from django.db import models
from main.models import WhoColumns

class Shpr(WhoColumns):
    cscode = models.CharField(max_length=7, unique=True)
    kind = models.CharField(max_length=1, blank=True)
    csname = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=120, blank=True)
    tel1 = models.CharField(max_length=20, blank=True)
    tel2 = models.CharField(max_length=20, blank=True)
    fax1 = models.CharField(max_length=20, blank=True)
    fax2 = models.CharField(max_length=20, blank=True)
    tlx = models.CharField(max_length=20, blank=True)
    attn = models.CharField(max_length=30, blank=True)
    dest = models.CharField(max_length=3, blank=True)
    shipno = models.CharField(max_length=7, blank=True)
    remark = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.cscode + '-' + self.csname
