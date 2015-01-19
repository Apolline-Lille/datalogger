#!/usr/bin/python

version='v0.0.0'

import string
import os
import subprocess
import argparse

##path and file name
#def get_file_name_base(module_name,current_time):
#  return time.strftime('%Y/%m/',current_time)+module_name+time.strftime('%Y_%m_%d',current_time)


list=subprocess.check_output(["ls","-lah"])
list=subprocess.check_output(["ls","-lah","/dev/serial/by-id"])
#list=subprocess.check_output(["bash","ls","-lah","/dev/serial/by-id/usb-*"])

print list
