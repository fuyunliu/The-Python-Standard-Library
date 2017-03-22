# -*- coding: utf-8 -*-

import sysconfig

for scheme in ['posix_prefix', 'posix_user']:
    print(scheme)
    print('=' * len(scheme))
    print('purelib =', sysconfig.get_path(name='purelib',
                                          scheme=scheme))
    print()
