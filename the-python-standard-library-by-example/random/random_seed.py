# -*- coding: utf-8 -*-

import random

random.seed(1)

# 多次运行产生的随机数是一样的
for i in range(5):
    print('%04.3f' % random.random())
print()
