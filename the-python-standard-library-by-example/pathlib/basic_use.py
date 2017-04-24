from pathlib import Path

p = Path('.')
print([x for x in p.iterdir() if x.is_file()])
print(list(p.glob('*.py')))

test = p / 'test' / 'test.txt'
print(test)
print(test.exists())

test = p / 'test.txt'

with test.open('wt') as f:
    f.write('hello')
