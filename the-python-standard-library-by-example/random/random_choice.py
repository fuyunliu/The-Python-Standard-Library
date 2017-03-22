# -*- coding: utf-8 -*-

import random

outcomes = {'heads': 0,
            'tails': 0,
            }
sides = outcomes.keys()

for i in range(10000):
    outcomes[random.choice(list(sides))] += 1

print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])
