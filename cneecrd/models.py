from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import WhoColumns
from custcsn.models import Custcsn

class Cneecrd(WhoColumns):
    custcsn = models.OneToOneField(Custcsn, on_delete=models.CASCADE, primary_key=True, related_name='cneecrd_custcsn')
    crdamt = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    aro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ars = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    arc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    arcod = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.custcsn.cuno + '-' + self.custcsn.cunme + '-' + str(self.crdamt)

@receiver(post_save, sender=Custcsn)
def create_custcsn_crdamt(sender, instance, created, **kwargs):
    if created:
        Cneecrd.objects.create(custcsn=instance, created_by=instance.created_by, last_updated_by=instance.last_updated_by)

# @receiver(post_save, sender=Custcsn)
# def save_custcsn_crdamt(sender, instance, **kwargs):
#     instance.cneecrd_custcsn.save()
