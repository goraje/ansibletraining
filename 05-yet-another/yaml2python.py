#!/usr/bin/env python

import yaml
import pprint
import argparse

# PARSE ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="path to aYAML file", type=str, default='template.yml')
args = parser.parse_args()

# PRINT THE ORIGINAL STRUCTURE TO THE TERMINAL
print('*** ORIGINAL YAML FILE ***\n')
sys.stdout.write(open(args.file,'r').read())

# FEW BLANK LINES FOR VISIBILITY
print('\n') * 3

# PRINT THE PYTHON INTERPRETATION OF THE FILE TO THE TERMINAL
print('*** PYTHON INTERPRETATION ***\n')
pprint.pprint(yaml.load(open(args.file)))
