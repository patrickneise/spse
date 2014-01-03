#!/usr/bin/python

import os

fileName = raw_input("Enter full path to file: ")

statinfo = os.stat(fileName)

print "File Size: " + str(statinfo.st_size)
