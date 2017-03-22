
import array
import binascii

s = 'This is the array.'
a = array.array('u', s)

print('As string:', s)
print('As array :', a)
print('As hex   :', binascii.hexlify(a))
