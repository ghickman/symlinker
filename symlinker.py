#!/usr/bin/python

__author__ = 'George Hickman'
__version__ = '0.2'

from optparse import OptionParser
import os

parser = OptionParser(usage="symlinker.py <start> <finish>",
                        version="Symlinker %s" % __version__)
options, args = parser.parse_args()

try:
    start = args[0]
    finish = args[1]
except IndexError:
    parser.error('Either a start or finish directory was not given')

for directory in os.listdir(start):
    origin = os.path.join(start, directory)+'/'
    destination = os.path.join(finish, directory)
    try:
        os.symlink(origin, destination)
    except OSError:
        continue
