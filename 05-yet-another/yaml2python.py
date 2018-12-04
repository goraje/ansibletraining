#!/usr/bin/env python

import argparse
import json
import yaml

from pprint import pformat
from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PyhthonLexer
from pygments.lexers.data import JsonLexer, YamlLexer

STYLE='rtt'

def pprint_python(obj):
    print(highlight(pformat(obj), PyhthonLexer(), Terminal256Formatter(style=STYLE)))

def pprint_json(obj):
    print(highlight(obj, JsonLexer(), Terminal256Formatter(style=STYLE)))

def pprint_yaml(obj):
    print(highlight(obj, YamlLexer(), Terminal256Formatter(style=STYLE)))

# PARSE ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="path to a YAML file", type=str, default='template.yml')
args = parser.parse_args()

# PRINT THE ORIGINAL STRUCTURE TO THE TERMINAL
print('\n============================')
print('***  ORIGINAL YAML FILE  ***')
print('============================\n')
pprint_yaml(open(args.file,'r').read())

# PRINT THE JSON EQUIVALENT
print('\n============================')
print('*** JSON FILE EQUIVALENT ***')
print('============================\n')
pprint_json(json.dumps(yaml.load(open(args.file)), indent=4, sort_keys=True))

# PRINT THE PYTHON INTERPRETATION OF THE FILE TO THE TERMINAL
print('\n=============================')
print('*** PYTHON INTERPRETATION ***')
print('=============================\n')
pprint_python(yaml.load(open(args.file)))
