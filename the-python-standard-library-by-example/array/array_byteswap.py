
import array
import binascii


def to_hex(a):
    chars_per_item = a.itemsize * 2  # 2 hex digits
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version) // chars_per_item
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        yield hex_version[start:end]


a1 = array.array('i', range(5))
a2 = array.array('i', range(5))
a2.byteswap()

fmt = '%10s %10s %10s %10s'
print(fmt % ('A1 hex', 'A1', 'A2 hex', 'A2'))
print(fmt % (('-' * 10,) * 4))
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt % values)
