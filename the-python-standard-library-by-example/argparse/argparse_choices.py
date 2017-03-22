
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--mode', choices=('read-only', 'read-write'))

print(parser.parse_args(['--mode', 'read-only']))
