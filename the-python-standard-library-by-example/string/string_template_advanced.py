# -*- coding: utf-8 -*-

import string

template_text = '''
  Delimiter : %%
  Replaced  : %with_underscore
  Ignored   : %notunderscored
'''

d = {'with_underscore': 'replaced',
     'notunderscored': 'not replaced',
     }


class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
