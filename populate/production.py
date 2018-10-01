
from populate import base
from account.models import User
from invpars.models import Invpars

print('Creating admin account ... ', end='')
User.objects.all().delete()
User.objects.create_superuser(username='admin', password='andyair', email=None, fullName='管理者')
print('done')

print('Creating Invoice parameters ... ', end='')
user = User.objects.first()
Invpars.objects.all().delete()
Invpars.objects.create(midno='81046553', mname='安抵航空貨運代理有限公司', taxno='81046553',
                       seqyy=0, seq01=0, seq02=0, seq03=0, seq04=0, seq05=0, seq06=0,
                       seq07=0, seq08=0, seq09=0, seq10=0, seq11=0, seq12=0,
                       created_by_id=user.id, last_updated_by_id=user.id)
print('done')
