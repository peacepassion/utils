#!/usr/bin/python

import sys
import os

ip = '10.64.41.139'
lp = '/swap'
wp = '.'
lf = '*'
wfs = []

send = True

debug = False

lg = len(sys.argv)
for i in range(1, lg, 1):
    if sys.argv[i] == '--ip':
        ip = sys.argv[i + 1]
    if sys.argv[i] == '-f':
        j = i + 1
        while j <= lg and sys.argv[j][0] != '-':
            wfs.append(sys.argv[j])
            j += 1
    if sys.argv[i] == '--lp':
        lp = sys.argv[i + 1]
    if sys.argv[i] == '--lf':
        lf = sys.argv[i+1]
    if sys.argv[i] == '--wp':
        wp = sys.argv[i+1]
    if sys.argv[i] == '-s':
        send = True
    if sys.argv[i] == '-r':
        send = False
    if sys.argv[i] == '-d':
        debug = True

if send is False:
    cmd = 'scp ' + 'root@' + ip + ':' + lp + '/' + lf + ' ' + wp
else:
    cmd = 'scp '
    for fl in wfs:
        cmd += fl + ' '
    cmd += 'root@' + ip + ':' + lp

if debug is True:
    print 'command: ' + cmd

os.system(cmd)
