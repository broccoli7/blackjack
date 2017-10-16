#!/usr/bin/python

import sys

if len(sys.argv) - 1 != 1:
    print 'Usage: ' + sys.argv[0] + ' <test-file.csv>'
    sys.exit(0)

with open(sys.argv[1], 'r') as infile:
    for line in infile:
        rows = line.rstrip().split(',')
        print rows[0]
