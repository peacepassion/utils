# README

All the script is used in Cygwin under Python 2.7.

#### add-py-al.py
Add an alias sentence in ~/.bashrc for convenient usage.  

Usage: python add-py-al.py [-d | --debug] [-t | --target-name=target-name] target-file  
-d: switch on debug mode  
-t: the name will be used as the alias name, default valued is the target-file name without surfix  
target-file: files will be handled  

#### rm_spc_file.py
Remove specified files with assigned surfix.  

Usage: python rm_spc_file.py [-d] [-p path] [-r] surfix  
-d: switch on debug mode  
-p: path will be worked in, default path is current working path  
-r: switch on recursive mode, default is off  
surfix: file surfix, e. g. exe  

#### sl.py
A pipe command to add line number in front of stdout.  

Usage: python sl.py file  
Can be used as a pipe command, e. g. echo 'hello python' | sl  

#### swap-file.py
A convenient method for swapping files between linux and cygwin by scp command.  
  
Usage: python [--ip ipaddress] [--wf windows-files] [--lp linux-path] [-s | -r] [-d]  
--ip: set ip  
--wf: if -s is set, the windows-files will be send  
--lp: set the linux path within which the files will be sent to or received from  
-s: send from windows to linux  
-r: received from linux to windows  
-d: switch on debug mode  

