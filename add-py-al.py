#!/usr/bin/python

__author__ = 'peace_da'

import os
import optparse


def usage():
    print 'usage: cmd [-t target-name] target-file'
    exit(1)


parser = optparse.OptionParser()
parser.add_option('-t', '--target-name', dest='t', default='')
parser.add_option('-d', '--debug', dest='debug', action='store_true', default=False)
opt, args = parser.parse_args()

if opt.debug is True:
    print 'opt: ' + str(opt)
    print 'args: ' + str(args)

if len(args) == 0:
    if opt.debug is True:
        print 'args is empty'
    usage()


def get_default_target_name():
    head, tail = os.path.split(args[0])
    df, ext = os.path.splitext(tail)
    return df


if opt.t == '':
    if opt.debug is True:
        print 'get default target name'
    opt.t = get_default_target_name()

if opt.debug is True:
    print 'target name is: ' + opt.t

full_name = os.path.abspath(args[0])
cmd = 'alias ' + opt.t + '=\'' + full_name + '\''
if opt.debug is True:
    print 'alias cmd: ' + cmd

home_path = os.path.expanduser('~')
if opt.debug is True:
    print 'home path is: ' + home_path

echo_cmd = 'echo \"' + cmd + '\"' + ' >> ' + home_path + '/.bashrc'
if opt.debug is True:
    print 'writing cmd: ' + echo_cmd

os.system(echo_cmd)

# source_cmd = 'source ' + '~/.bashrc'
# if opt.debug is True:
#     print 'source cmd: ' + source_cmd
#
# cmd = echo_cmd + ' && ' + source_cmd
# if opt.debug is True:
#     print 'cmd: ' + cmd

# os.system(cmd)

# os.popen(cmd)






















