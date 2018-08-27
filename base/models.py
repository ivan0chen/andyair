from django.db import models
from datetime import datetime

class Custadv(models.Model):
    cuno = models.CharField(max_length=10, unique=True)        #客戶代號
    ipntfy = models.CharField(max_length=30, blank=True)       #應通知公司
    ipntfym = models.CharField(max_length=30, blank=True)      #貨主聯絡人
    ipntftl = models.CharField(max_length=20, blank=True)      #電話號碼
    ipntffx = models.CharField(max_length=20, blank=True)      #傳真號碼
    ipmnspay = models.BooleanField(blank=True)                 #是否月結
    ipentry = models.BooleanField(blank=True)                  #是否報關
    iprtord = models.BooleanField(blank=True)                  #是否進口指定貨
    ipntfmk = models.CharField(max_length=30, blank=True)      #備註
    creation_date = models.DateTimeField(auto_now_add=True)    #建立日期
    created_by = models.IntegerField(default=1)                #建立者
    last_update_date = models.DateTimeField(auto_now=True)     #最後更新日期
    last_updated_by = models.IntegerField(default=1)           #最後更新者

    def __str__(self):
        return self.cuno + '-' + self.ipntfy

class Custqtn(models.Model):
    custadv = models.ForeignKey(Custadv, on_delete=models.CASCADE)
    org = models.CharField(max_length=3)                       #ORG
    qtndd = models.DateTimeField(blank=True)                   #日期
    qtns = models.CharField(max_length=60, blank=True)         #說明
    creation_date = models.DateTimeField(auto_now_add=True)    #建立日期
    created_by = models.IntegerField(default=1)                #建立者
    last_update_date = models.DateTimeField(auto_now=True)     #最後更新日期
    last_updated_by = models.IntegerField(default=1)           #最後更新者
    trashed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.org + '--' + self.qtndd.strftime('%Y-%m-%d')
