# -*- coding: utf-8 -*-

import json
from io import StringIO

f = StringIO('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
print(json.load(f))
