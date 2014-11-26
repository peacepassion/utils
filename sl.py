#!/usr/bin/python

__author__ = 'peace_da'

import sys
import os

content = sys.stdin.read(-1)

cmd = "grep --color -n -i ''"

stdin = os.popen(cmd, 'w')

try:
    stdin.write(content)
finally:
    stdin.close()





