from all_test.setting.base import * # NOQA
from django.conf import settings

if __name__ == '__main__':
    DEBUG = True
    xx = settings.__getattr__('ZTDS_SYSTEM')
    print(xx)
