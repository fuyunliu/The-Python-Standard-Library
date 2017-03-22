# -*- coding: utf-8 -*-

import sysconfig

for name in sysconfig.get_path_names():
    print(name)
