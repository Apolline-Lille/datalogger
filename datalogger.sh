#!/bin/bash

for dev in /dev/ttyUSB?
do
  echo 'start logging '$dev
  nohup ./datalogger.py --device $dev &
  sleep 1
done

#wait
sleep 2

#check
ps aux | grep datalogger.py
