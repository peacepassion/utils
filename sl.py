#!/usr/bin/python

from __future__ import print_function
import sys
import os
import fileinput

# this is a good method using os command
# content = sys.stdin.read(-1)
#
# cmd = "grep --color -n -i ''"
#
# stdin = os.popen(cmd, 'w')
#
# try:
# stdin.write(content)
# finally:
# stdin.close()


for line in fileinput.input():
    print(str(str(fileinput.lineno()) + ':').rjust(3), line, sep=' ', end='')





