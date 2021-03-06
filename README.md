# README

All the script is used in Cygwin under Python 2.7.

#### add-py-al.py
######Add an alias sentence in ~/.bashrc for convenient usage.  
Usage: python add-py-al.py [-d | --debug] [-t | --target-name=target-name] target-file  
-d: switch on debug mode  
-t: the name will be used as the alias name, default valued is the target-file name without suffix  
target-file: files will be handled  

#### rm_spc_file.py
######Remove specified files with assigned suffix.  
Usage: python rm_spc_file.py [-d] [-p path] [-r] suffix  
-d: switch on debug mode  
-p: path will be worked in, default path is current working path  
-r: switch on recursive mode, default is off  
suffix: file suffix, e. g. exe  

#### sl.py
######A pipe command to add line number in front of stdout.  
Usage: python sl.py file  
Can be used as a pipe command, e. g. echo 'hello python' | sl  

#### swap-file.py
######A convenient method for swapping files between linux and cygwin by scp command.  
Usage: python swap-file.py [--ip ipaddress] [--wf windows-files] [--lp linux-path] [-s | -r] [-d]
--ip: set ip  
--wf: if -s is set, the windows-files will be send  
--lp: set the linux path within which the files will be sent to or received from  
-s: send from windows to linux  
-r: received from linux to windows  
-d: switch on debug mode  

#### mv-swap.py
######Used in Linux, move files to a specified dir for Win get files by scp command by Cygwin.  
Usage: python mv-swap.py [-c | --clear] [-p | --path] [-d | --debug] file...
-c: clear the path set by -p  
-p: a path used for swapping  
-d: switch on debug mode  
file: target files  

#### p4-build.py
######Used in Linux, automate perforce login, perforce checkout code, and execute build script
Usage: python [-d | --debug] [-b | --build-script build-script] build-arg
-d: switch on debug mode
-b: set build script
build-arg: argument for build script

#### create-singleton.py
######Used in Linux, creating necessary singleton sentences for an existing Java class, mainly supporting Android development.
Usage: python create-singleton.py [-d | --debug] [-c | --no-context] [-s | --no-synchronized] target-file...  
-d: switch on debug mode  
-c: do not put Context as constructor parameter  
-s: do not need sync singleton method  
target-file: Java files need to be handled  

#### git-pipe.py
######Used in Linux, read pipe input as git command input
Usage: python git-pipe.py [-d | --debug] [-s | --space] git-command...  
-d: switch on debug mode  
-s: there is space in pipe input  
git-command: e.g. git add  
e.g. git status | grep modified | cut -b 16- | python git-pipe.py -d 'git add'  