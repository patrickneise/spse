#!/usr/bin/python

fdesc = open("/var/log/messages", "r")

for line in fdesc.readlines():
    if "usb" in line:
        print line.strip()
