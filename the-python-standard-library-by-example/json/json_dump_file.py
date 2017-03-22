# -*- coding: utf-8 -*-

import json
from io import StringIO

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

f = StringIO()
json.dump(data, f)

print(f.getvalue())
