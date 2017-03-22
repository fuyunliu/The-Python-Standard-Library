
import bisect
import random

# Reset the seed
random.seed(1)

print('New  Pos  Contents')
print('---  ---  --------')

# Use bisect_left and insort_left.
l = []
for i in range(1, 15):
    r = random.randint(1, 100)
    position = bisect.bisect_left(l, r)
    bisect.insort_left(l, r)
    print('%3d  %3d' % (r, position), l)
