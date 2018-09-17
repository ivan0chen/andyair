from django.db import models
# from django.utils import timezone
from datetime import datetime
from account.models import User

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

