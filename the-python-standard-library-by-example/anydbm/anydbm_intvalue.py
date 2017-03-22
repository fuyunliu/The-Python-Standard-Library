
import dbm


with dbm.open('example.db', 'c') as db:
    try:
        db['one'] = 1
    except TypeError as e:
        print('%s: %s' % (e.__class__.__name__, e))
