#!/usr/bin/python


import optparse
import os

opt_obj = optparse.OptionParser()
opt_obj.add_option('-d', '--debug', action='store_true', dest='debug', default=False, help='switch on debug mode')
opt_obj.add_option('-b', '--build-script', dest='build_script', default='', help='set build script')
opt, args = opt_obj.parse_args()

if opt.debug is True:
    print 'opt: ', opt
    print 'arg: ', args

if os.path.isfile(opt.build_script) is False:
    print 'build script is illegal'
    exit(4)

cmd1 = 'p4 sync -f ...'
if opt.debug is True:
    print 'p4 sync command is: ' + cmd1

ret = os.system(cmd1)

if ret != 0:
    cmd4 = 'p4 login'
    if opt.debug is True:
        print 'p4 login command: ', cmd4
    ret = os.system(cmd4)
    if ret != 0:
        print 'p4 login error, command: ', cmd4
        exit(4)
    ret = os.system(cmd1)
    if ret != 0:
        print 'p4 sync error, command: ', cmd1
        exit(1)

cmd2 = 'chmod +x ' + opt.build_script
if opt.debug is True:
    print 'chmod command: ', cmd2

ret = os.system(cmd2)

if ret != 0:
    print 'chmod failed', ' chmod: ' + cmd2
    exit(2)

build_script_abs_path = os.path.abspath(opt.build_script)
cmd3 = build_script_abs_path + ' '
for arg in args:
    cmd3 += arg + ' '

if opt.debug is True:
    print 'build command: ' + cmd3

ret = os.system(cmd3)

if ret != 0:
    print 'build failed', ' command: ' + cmd3
    exit(3)
