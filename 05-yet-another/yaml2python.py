#!/usr/bin/env python

import sys
import yaml
import pprint

# SHOW USAGE INFO
if sys.argv[1] in ['-h', '--help']:
    print('USAGE: ./yaml2python.py [YAML_FILE_PATH]')

# LOAD THE YAML FILE
f = open(sys.argv[1])

# PRINT THE ORIGINAL STRUCTURE TO THE TERMINAL
print('*** ORIGINAL YAML FILE ***\n')
sys.stdout.write(f.read())

# FEW BLANK LINES FOR VISIBILITY
print('\n') * 3

# PRINT THE PYTHON INTERPRETATION OF THE FILE TO THE TERMINAL
print('*** PYTHON INTERPRETATION ***\n')
pprint.pprint(yaml.load(f))
