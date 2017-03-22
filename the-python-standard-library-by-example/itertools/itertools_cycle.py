
from itertools import *

for i, item in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i, item)
