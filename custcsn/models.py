from django.db import models
from main.models import WhoColumns


class Custcsn(WhoColumns):
    cuno = models.CharField(max_length=10, unique=True)
    cucd = models.CharField(max_length=1, blank=True)
    cunme = models.CharField(max_length=40, blank=True)
    cuid = models.CharField(max_length=8, blank=True)
    cunmc = models.CharField(max_length=40, blank=True)
    cuchadd1 = models.CharField(max_length=30, blank=True)
    cuchadd2 = models.CharField(max_length=30, blank=True)
    cuenadd1 = models.CharField(max_length=30, blank=True)
    cuenadd2 = models.CharField(max_length=30, blank=True)
    cuenadd3 = models.CharField(max_length=30, blank=True)
    cudir = models.CharField(max_length=20, blank=True)
    cutel = models.CharField(max_length=20, blank=True)
    cufax = models.CharField(max_length=20, blank=True)
    cupcfax = models.CharField(max_length=20, blank=True)
    cuattn = models.CharField(max_length=30, blank=True)
    cunminv = models.CharField(max_length=40, blank=True)
    cusale = models.CharField(max_length=8, blank=True)
    custmk = models.CharField(max_length=40, blank=True)
    cucgdt = models.DateTimeField(auto_now_add=True, editable = True)
    cucrdt = models.DateTimeField(auto_now=True, editable = True)
    cutrdt = models.DateTimeField(auto_now=True, editable = True)

    # cucgdt.editable = True
    # cucrdt.editable = True
    # cutrdt.editable = True

    def __str__(self):
        return self.cuno + ' - ' + self.cunme
