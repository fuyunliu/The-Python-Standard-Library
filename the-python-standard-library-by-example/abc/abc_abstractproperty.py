# -*- coding: utf-8 -*-

import abc


class Base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def value(self):
        return 'Should never get here'

    @abc.abstractproperty
    def constant(self):
        return 'Should never get here'


class Implementation(Base):
    @property
    def value(self):
        return 'concrete property'

    constant = 'set by a class attribute'


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as e:
    print('ERROR:', str(e))

i = Implementation()
print('Implementation.value   :', i.value)
print('Implementation.constant:', i.constant)
