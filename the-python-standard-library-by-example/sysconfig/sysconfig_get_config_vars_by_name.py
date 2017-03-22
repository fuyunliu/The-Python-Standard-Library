# -*- coding: utf-8 -*-

import sysconfig

bases = sysconfig.get_config_vars('base', 'platbase', 'userbase')
print('Base directories:')
for b in bases:
    print('   ', b)
