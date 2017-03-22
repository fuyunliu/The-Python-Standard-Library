# -*- coding: utf-8 -*-

import base64

# Load this source file and strip the header.
with open(__file__, 'rt') as input:
    raw = input.readline()
    initial_data = raw.encode('ascii')

encoded_data = base64.b64encode(initial_data)

num_initial = len(initial_data)

# There will never be more than 2 padding bytes.
padding = 3 - (num_initial % 3)

print('%d bytes before encoding' % num_initial)
print('Expect %d padding bytes' % padding)
print('%d bytes after encoding' % len(encoded_data))
print()
print(encoded_data)
print(initial_data)
