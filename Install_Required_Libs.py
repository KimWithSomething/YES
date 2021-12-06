import os
from Operations import File
from Operations import python2
import easygui



p = easygui.ynbox('we need some Libs to install do we have your permisson to install them?', 'Install Needed Lib or Resources', ('Yes', 'No'))
Needed_Libs =['tkinter','Path','easygui']
'''print('Hello we need some Libs to install do we have your permisson to install them? [y/n]')
Permisson = input('')'''

if p == True:
    python2.Install_Plugins(Needed_Libs,len(Needed_Libs))
else:
    exit()