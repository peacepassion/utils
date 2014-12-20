#!/usr/bin/python

import optparse
import os
import re
import fileinput


def write_singleton(_class_name, _need_context, _need_sync, _indentation):
    indents = []
    indent_unit = ''
    for i in range(_indentation):
        indent_unit += ' '
    for i in range(1, 6, 1):
        indents.append(indent_unit * i)

    print ''
    print indents[0] + 'private static ' + _class_name + ' sInstance;'
    print ''
    if _need_context:
        print indents[0] + 'private Context mContext;'
        print ''
    print indents[0] + 'private ' + _class_name + '(' + ('Context ctx' if _need_context else '') + ') {'
    print indents[1] + 'mContext = ctx;' if _need_context else ''
    print indents[0] + '}'
    print ''
    print indents[0] + 'public static ' + _class_name + ' ' + 'getInstance(' + (
        'Context ctx' if _need_context else '') + ') {'
    print indents[1] + 'if (sInstance == null) {'
    if _need_sync:
        print indents[2] + 'synchronized(' + _class_name + '.class) {'
        print indents[3] + 'if (sInstance == null) {'
    print (indents[4] if _need_sync else indents[2]) + 'sInstance = new ' + _class_name + '(' + (
        'ctx' if _need_context else '') + ');'
    print (indents[3] if _need_sync else indents[1]) + '}'
    if _need_sync:
        print indents[2] + '}'
        print indents[1] + '}'
    print indents[1] + 'return sInstance;'
    print indents[0] + '}'


def write_file(_fl):
    path, fn = os.path.split(_fl)
    file_root, ext = os.path.splitext(fn)
    pattern = r'((\s+class)|(^class))\s+(?P<class_name>\w+)'
    compiled_pattern = re.compile(pattern)
    class_name = ''
    start_next_line = False
    for line in fileinput.input(_fl, inplace=True, backup=''):
        match = compiled_pattern.search(line)
        if match is not None:
            class_name = match.groupdict()['class_name']
            if cmp(class_name, file_root) == 0:
                if opt.context:
                    print 'import android.content.Context;'
                    print ''
                print line,
                pattern2 = r'{\s*$'
                compiled_pattern2 = re.compile(pattern2)
                if len(compiled_pattern2.findall(line)) != 0:
                    write_singleton(class_name, opt.context, opt.sync, opt.indentation)
                else:
                    start_next_line = True
        else:
            print line,
            if start_next_line is True:
                write_singleton(class_name, opt.context, opt.sync, opt.indentation)
                start_next_line = False
    if opt.debug:
        print 'class name: ', class_name
    if cmp(class_name, '') == 0:
        print 'failed to find class name'
        return
    if cmp(class_name, file_root) != 0:
        print _fl, ' is illegal: its filename does not equal class name'


parser = optparse.OptionParser()
parser.add_option('-d', '--debug', dest='debug', action='store_true', default=False, help='switch on debug mode')
parser.add_option('-c', '--no-context', dest='context', action='store_false', default=True,
                  help='do not put Context as parameter')
parser.add_option('-s', '--no-synchronized', dest='sync', action='store_false', default=True,
                  help='do not need synchronization')
parser.add_option('-i', '--indentation', dest='indentation', default=4, help='set indentation')
opt, arg = parser.parse_args()

if opt.debug:
    print 'opt: ', opt
    print 'arg: ', arg

if len(arg) == 0:
    print 'no target file'
    exit(1)

java_files = []
for target_file in arg:
    fn, ext = os.path.splitext(target_file)
    if opt.debug:
        print 'file name: ', fn
        print 'file ext: ', ext
    if cmp(ext, '.java') != 0:
        print 'Only support Java file.', target_file + ' is not supported'
    else:
        write_file(target_file)










