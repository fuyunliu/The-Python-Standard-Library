# -*- coding: utf-8 -*-

import base64

original_string = b'This is the data, in the clear.'
print('Original:', original_string)

encoded_string = base64.b32encode(original_string)
print('Encoded :', encoded_string)

decoded_string = base64.b32decode(encoded_string)
print('Decoded :', decoded_string)
