from django.db import models
from main.models import WhoColumns

class Inprmk(WhoColumns):
    code = models.CharField(max_length=3, unique=True)
    state = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.code + '-' + self.state
