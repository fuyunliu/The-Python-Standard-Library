
import hashlib

from hashlib_data import lorem


data = "http://www.sdbid.cn/BiddingChange/Detail/170036"
h = hashlib.md5()
h.update(lorem.encode())
print(h.hexdigest())
print()

print(hashlib.md5(data.encode()).hexdigest() + '.txt')
