
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=int)
parser.add_argument('-f', type=float)
parser.add_argument('--file', type=argparse.FileType('r'))

try:
    print(parser.parse_args())
except IOError as msg:
    parser.error(str(msg))
