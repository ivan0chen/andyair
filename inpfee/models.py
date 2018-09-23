from django.db import models
from main.models import WhoColumns

class Inpfee(WhoColumns):
    code = models.CharField(max_length=3, unique=True)
    state = models.CharField(max_length=30, blank=True)
    tax =   models.CharField(max_length=1, blank=True)
    ocamt = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)

    def __str__(self):
        return self.code + '-' + self.state