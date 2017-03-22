# -*- coding: utf-8 -*-

import sysconfig
import sys

print('sysconfig.get_python_version():', sysconfig.get_python_version())
print('\nsys.version_info:')
print('  major       :', sys.version_info.major)
print('  minor       :', sys.version_info.minor)
print('  micro       :', sys.version_info.micro)
print('  releaselevel:', sys.version_info.releaselevel)
print('  serial      :', sys.version_info.serial)
