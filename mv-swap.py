#!/usr/bin/python

import os
import optparse

parser = optparse.OptionParser()
parser.add_option('-c', '--clear', action='store_true', dest='is_clr', default='False',
                  help='set if target path should be cleared')
parser.add_option('-p', '--path', action='store', dest='target_path', default='/swap',
                  help='set target path that where the files will be put')
parser.add_option('-d', '--debug', action='store_true', dest='debug', default='False',
                  help='switch on debug mode')

opt, arg = parser.parse_args()

if opt.debug is True:
    print 'opt: ', opt
    print 'arg: ', arg

if opt.is_clr is True:
    clr_cmd = 'rm -f ' + opt.target_path + '/* '
    if opt.debug is True:
        print('clear command: ' + clr_cmd)
    os.system(clr_cmd)

if len(arg) == 0:
    print 'Target files should be set.'
    exit(1)

cp_cmd = 'cp -rv '
for fl in arg:
    cp_cmd += fl + ' '

cp_cmd += opt.target_path

if opt.debug is True:
    print('copy command: ' + cp_cmd)

os.system(cp_cmd)
