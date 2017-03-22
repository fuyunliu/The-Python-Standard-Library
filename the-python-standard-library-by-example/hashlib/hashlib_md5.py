
import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode())
print(h.hexdigest())
