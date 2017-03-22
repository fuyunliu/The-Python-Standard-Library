import atexit
import os


def not_called():
    print('This should not be called')


print('Registering')
atexit.register(not_called)
print('Registered')

print('Exiting...')
os._exit(0)
