import atexit


def my_cleanup(name):
    print('my_cleanup(%s)' % name)


atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')
