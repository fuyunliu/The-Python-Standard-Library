# -*- coding: utf-8 -*-

import os
import logging


LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'debug.log')
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )


logging.info('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()


print('FILE:')
print(body)
