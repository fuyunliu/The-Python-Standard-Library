
import pickle
from io import BytesIO


class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO
out_s = BytesIO()

# Write to the stream
for o in data:
    print('WRITING : %s (%s)' % (o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Set up a read-able stream
in_s = BytesIO(out_s.getvalue())

# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ    : %s (%s)' % (o.name, o.name_backwards))
