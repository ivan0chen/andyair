from django.db import models
from main.models import WhoColumns

class Custadv(WhoColumns):
    cuno = models.CharField(max_length=10, unique=True)        #客戶代號
    ipntfy = models.CharField(max_length=30, blank=True)       #應通知公司
    ipntfym = models.CharField(max_length=30, blank=True)      #貨主聯絡人
    ipntftl = models.CharField(max_length=20, blank=True)      #電話號碼
    ipntffx = models.CharField(max_length=20, blank=True)      #傳真號碼
    ipmnspay = models.BooleanField(blank=True)                 #是否月結
    ipentry = models.BooleanField(blank=True)                  #是否報關
    iprtord = models.BooleanField(blank=True)                  #是否進口指定貨
    ipntfmk = models.CharField(max_length=30, blank=True)      #備註

    def __str__(self):
        return self.cuno + '-' + self.ipntfy

class Custqtn(WhoColumns):
    custadv = models.ForeignKey(Custadv, on_delete=models.CASCADE)
    org = models.CharField(max_length=3)                       #ORG
    qtndd = models.DateTimeField(blank=True)                   #日期
    qtns = models.CharField(max_length=60, blank=True)         #說明
    trashed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.org + '--' + self.qtndd.strftime('%Y-%m-%d')
