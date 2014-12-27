#!/usr/bin/python

import optparse
import sys
import os

parser = optparse.OptionParser()
parser.add_option('-d', '--debug', dest='debug', action='store_true', default=False)
parser.add_option('-s', '--space', dest='space', action='store_true', default=False)
opt, args = parser.parse_args()

if opt.debug:
    print 'opt: ', opt
    print 'arg: ', args

target = sys.stdin.read(-1)
if opt.debug:
    print 'stdin: ', target

cmd = ''
for arg in args:
    cmd += arg + ' '

if opt.space:
    target = '"' + target + '"'

cmd += target

if opt.debug:
    print 'cmd: ', cmd

os.system(cmd)
