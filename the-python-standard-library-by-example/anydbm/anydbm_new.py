
import dbm


# 打开模式有：'r', 'w', 'c', 'n'
with dbm.open('example.db', 'c') as db:

    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    assert db[b'hello'] == b'there'
    assert db[b'www.python.org'] == b'Python Website'
    assert db['www.cnn.com'] == b'Cable News Network'

    print(db.get('python.org', b'not present'))

    # key 和 value 必须都是字符串
    db['www.yahoo.com'] = '123456'
