
import dbm


with dbm.open('example.db', 'w') as db:
    try:
        db[1] = 'one'
    except TypeError as e:
        print('%s: %s' % (e.__class__.__name__, e))
