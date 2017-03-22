# -*- coding: utf-8 -*-

import random
import time

print('Default initializiation:\n')

r1 = random.Random()
r2 = random.Random()

for i in range(3):
    print('%04.3f  %04.3f' % (r1.random(), r2.random()))

print('\nSame seed:\n')

seed = time.time()
r1 = random.Random(seed)
r2 = random.Random(seed)

for i in range(3):
    print('%04.3f  %04.3f' % (r1.random(), r2.random()))
