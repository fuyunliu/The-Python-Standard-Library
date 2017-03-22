
import pickle
import sys


class SimpleObject(object):
    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]


if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('cPickle'))
    data.append(SimpleObject('last'))

    filename = sys.argv[1]

    with open(filename, 'wb') as out_s:
        # Write to the stream
        for o in data:
            print('WRITING: %s (%s)' % (o.name, o.name_backwards))
            pickle.dump(o, out_s)
