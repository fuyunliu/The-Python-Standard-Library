
import dbm

with dbm.open('example.db', 'r') as db:
    print('keys():', db.keys())
    for k, v in db.items():
        print('iterating:', k, v)
    print('db["hello"] =', db['hello'])
