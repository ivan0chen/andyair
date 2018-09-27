
from populate import base
from invpars.models import Invpars

def populate():
    print('Creating Invoice parameters ... ', end='')
    Invpars.objects.all().delete()
    Invpars.objects.create(midno='81046553', mname='安抵航空貨運代理有限公司', taxno='81046553',
                           seqyy=0, seq01=0, seq02=0, seq03=0, seq04=0, seq05=0, seq06=0,
                           seq07=0, seq08=0, seq09=0, seq10=0, seq11=0, seq12=0)
    print('done')

if __name__ == '__main__':
    populate()