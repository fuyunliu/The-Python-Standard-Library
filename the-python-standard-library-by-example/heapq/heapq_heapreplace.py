
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data


heapq.heapify(data)
print('start:')
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace %2d with %2d:' % (smallest, n))
    show_tree(data)
