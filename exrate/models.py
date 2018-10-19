from django.db import models
from main.models import WhoColumns

class Exrate(WhoColumns):
    code = models.CharField(max_length=3, unique=True)
    currency = models.CharField(max_length=25, blank=True)
    ex_irate = models.DecimalField(max_digits=9, decimal_places=5, null=True, blank=True)
    ex_orate = models.DecimalField(max_digits=9, decimal_places=5, null=True, blank=True)
    lastdate = models.DateField(null=True, blank=True)

    def __str__(self):
        # return self.code
        return self.code + '-' + self.currency + ' ( ' + str(self.lastdate) + ' ) : ' + str(self.ex_irate) + ' - ' + str(self.ex_orate)

