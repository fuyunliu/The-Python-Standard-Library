# -*- coding: utf-8 -*-

import string

for name in (s for s in dir(string) if not s.startswith('_')):
    value = getattr(string, name)
    # Look for byte string and unicode values
    if isinstance(value, str):
        print('%s=%r\n' % (name, value))
