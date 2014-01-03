#!/usr/bin/python

import os

def printDir(dir, indent):
    for item in os.listdir(dir):
        if os.path.isdir(os.path.join(dir,item)):
            print indent + item
            indent += "----"
            printDir(os.path.join(dir,item),indent)
            indent = indent[-4:]
        elif os.path.isfile(item):
            print indent + item
        else:
            print indent + item

usrdir = raw_input("Enter dir: ")

indent = ""

printDir(usrdir, indent)
