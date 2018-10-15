from django.db import models
from account.models import User

class OrgDest(models.Model):
    code5 = models.CharField(max_length=5, unique=True)
    code = models.CharField(max_length=3, unique=True)
    dest = models.CharField(max_length=30, blank=True)
    iso = models.CharField(max_length=2, blank=True)
    country = models.CharField(max_length=20, blank=True)
    aircode = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.code + ' - ' + self.dest


class WhoColumns(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)         # 建立日期
    created_by = models.ForeignKey(User, editable=False,
                                   db_column='created_by',
                                   related_name='%(app_label)s_%(class)s_created_by',
                                   blank=True, null=True,
                                   on_delete=models.SET_NULL)    #建立者

    last_update_date = models.DateTimeField(auto_now=True)          # 最後更新日期
    last_updated_by = models.ForeignKey(User, editable=False,
                                        db_column='last_updated_by',
                                        related_name='%(app_label)s_%(class)s_last_updated_by',
                                        blank=True, null=True,
                                        on_delete=models.SET_NULL)  # 最後更新者


    # def save(self, *args, **kwargs):
    #     if not self.creation_date:
    #         self.creation_date = datetime.now()
    #
    #     self.last_update_date = datetime.now()
    #     return super(WhoColumns, self).save(*args, **kwargs)

    class Meta:
        abstract = True

