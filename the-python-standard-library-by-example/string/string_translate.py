# -*- coding: utf-8 -*-

intab = 'aeiou'
outtab = '12345'

s = 'this is string example....wow!!!'

print(s.translate({ord(x): y for (x, y) in zip(intab, outtab)}))
