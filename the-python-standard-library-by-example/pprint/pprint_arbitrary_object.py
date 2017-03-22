# -*- coding: utf-8 -*-

from pprint import pprint


class node(object):
    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return ('node(' + repr(self.name) + ', ' +
                repr(self.contents) + ')'
                )


trees = [node('node-1'),
         node('node-2', [node('node-2-1')]),
         node('node-3', [node('node-3-1')]),
         ]
pprint(trees)
