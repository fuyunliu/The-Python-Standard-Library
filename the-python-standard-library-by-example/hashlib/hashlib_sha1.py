
import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode())
print(h.hexdigest())
