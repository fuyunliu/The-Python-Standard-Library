# -*- coding: utf-8 -*-

import dbm

db = dbm.open('test.db', 'n')
db['key'] = 'value'
db.close()

print((dbm.whichdb('test.db')))
