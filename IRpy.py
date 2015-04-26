#!/usr/bin/python
#   Title: IRpy.py
#   Author: Grominet
#   Date: 26-04-2015
#   Info: Manage LIRC from a python script
#   URL : 
#   Version : 0.1
#
# Needs : LIRC installed and up
# Use it for Domoticz
#
# How to exemple :
# in a switch Action On : script:///home/pi/domoticz/scripts/IRpy.py send_once philips_RC28242501 KEY_POWER 1

 
import os
import sys
import datetime
 
# If enabled. The script will log to the file _.log
log_to_file = False
 

# DO NOT CHANGE BEYOND THIS LINE
if len(sys.argv) < 4 :
  print ("Not enough parameters. Needs %directive (send_once) %remote %key_code %repeat")
  sys.exit(0)


directive = sys.argv[1]
remote = sys.argv[2]
code = sys.argv[3]

if len(sys.argv) == 5:
  count = sys.argv[4]
else:
  count=1

#print "dir:"+directive
#print "rem:"+remote
#print "code:"+code
#print "count:"+str(count)

def log(message):
  print message
  if log_to_file == True:
    logfile = open('IRpy.log', "a")
    logfile.write(message + "\n")
    logfile.close()
 
 
cmd = "irsend "+directive+" "+remote+" "+code+" -# "+str(count)
#print "cmd:"+cmd

os.system(cmd)
log(datetime.datetime.now().strftime("%H:%M:%S") +" IRpy "+ directive+" "+remote+" "+code +" sent")

