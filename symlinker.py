#!/usr/bin/python

__author__ = 'George Hickman'
__version__ = '0.1'

import os

start = '/path/to/start'
finish = '/path/to/finish'

for directory in os.listdir(start):
    origin = os.path.join(start, directory)+'/'
    destination = os.path.join(finish, directory)
    try:
        os.symlink(origin, destination)
    except OSError:
        continue
