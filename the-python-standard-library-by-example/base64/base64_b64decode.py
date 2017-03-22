# -*- coding: utf-8 -*-

import base64

original_string = b'This is the data, in the clear.'
print('Original:', original_string)

# 编码
encoded_string = base64.b64encode(original_string)
print('Encoded :', encoded_string)

# 解码
decoded_string = base64.b64decode(encoded_string)
print('Decoded :', decoded_string)
