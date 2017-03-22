
from itertools import *
from operator import itemgetter

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.items(), key=itemgetter(1))


for k, g in groupby(di, key=itemgetter(1)):
    print(k, list(map(itemgetter(0), g)))
