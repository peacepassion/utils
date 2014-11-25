__author__ = 'peace_da'

import sys, os, glob, shutil

# for file in glob.glob('*.' + sys.argv[1]):
# os.remove(file)

# files = os.listdir('.')
# print 'file num: ' + str(len(files))

# for file in os.listdir('.'):
# root, ext = os.path.split(file)
# # if ext[1:] == sys.argv[1]:
# if cmp(ext[1:], sys.argv[1]) == 0:
# os.remove(file)

def rmFile(surfix, dirname, fnames):
#    print 'dirname: ', dirname
#    print 'curent path: ', os.curdir
    for fname in fnames:
        base, ext = os.path.splitext(fname)
        # print 'ext: ', ext
        if cmp(ext[1:], surfix) == 0:
            print 'removing file: ', fname
            # if os.path.exists(file):
            os.remove(os.path.join(dirname, fname))

if __name__ == '__main__':
    os.path.walk(os.getcwd(), rmFile, sys.argv[1])

