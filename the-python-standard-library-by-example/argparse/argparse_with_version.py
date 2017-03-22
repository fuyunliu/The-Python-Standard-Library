
import argparse

parser = argparse.ArgumentParser(prog='PROG')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
parser.add_argument('--version', action='version', version='%(prog)s 2.0')


print(parser.parse_args(['--version']))

print('This is not printed')
