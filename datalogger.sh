#!/bin/bash

for devbyid in /dev/serial/by-id/usb-*
do
  dev=`ls -lah $devbyid | tail -c 8` #e.g. ttyUSB0 or ttyACM0
  dev=/dev/$dev
  if((`echo $devbyid | grep Arduino | wc -l`>0)) #Arduino #UNO
  then
    echo $devbyid
    echo $dev" is Arduino #UNO"
  fi

#  Arduino #UNO
#  Prolific #DYLOS
#  AM01 #AlphaSense CO2

  echo 'start logging '$dev'.'
#  nohup ./datalogger.py --device $dev &
  sleep 1
done

#wait
sleep 2

#check
ps aux | grep '.py' | grep datalogger --color
