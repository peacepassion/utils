#!/usr/bin/python

__author__ = 'peace_da'

import sys
import os
import getopt
import glob

sfxs = []
path = '.'
debug = False
recursive = False
fls = []

try:
    opts, args = getopt.getopt(sys.argv[1:], 'p:dr')
except getopt.GetoptError as ep:
    print(ep.message)

for opt, val in opts:
    if opt == '-p':
        path = val
        if path is None or len(path) == 0:
            print '-p should offer a path'
            sys.exit(1)
    if opt == '-d':
        debug = True
    if opt == '-r':
        recursive = True

for val in args:
    sfxs.append(val)
if len(sfxs) == 0:
    print 'should offer suffix for specified files'
    sys.exit(2)

if debug is True:
    print 'opts: ' + str(opts)
    print 'args: ' + str(args)


def rm_fl(local_sfxs, dir_name, fnames):
    for local_sfx in local_sfxs:
        local_p = dir_name + '/*.' + local_sfx
        fls.extend(glob.glob(local_p))


if recursive is not True:
    print 'no recursive'
    if path[0] == '/':
        for sfx in sfxs:
            p = path[0] + '/*.' + sfx
            fls.extend(glob.glob(p))
            if debug is True:
                print 'abs path, match pattern: ' + p
    else:
        for sfx in sfxs:
            p = os.path.join(os.getcwd(), path[0])
            p += '/*.' + sfx
            fls.extend(glob.glob(p))
            if debug is True:
                print 'rel path, match pattern: ' + p
else:
    print 'recursive'
    os.path.walk(os.getcwd(), rm_fl, sfxs)

for fl in fls:
    if debug is True:
        print 'removing file: ' + fl
    os.remove(fl)

