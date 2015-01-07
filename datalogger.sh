#!/bin/bash

for devbyid in /dev/serial/by-id/usb-*
do
  dev=`ls -lah $devbyid | tail -c 8` #e.g. ttyUSB0 or ttyACM0
  dev=/dev/$dev
  #switch datalogger depending on device
#  echo $devbyid
  ##Arduino #UNO
  if((`echo $devbyid | grep Arduino | wc -l`>0))
  then
    echo $dev" is Arduino #UNO"
    datalogger=./datalogger_UNO.py
  fi
  ##Prolific #DYLOS
  if((`echo $devbyid | grep Prolific | wc -l`>0))
  then
    echo $dev" is Prolific #DYLOS"
    datalogger=./datalogger_DYLOS.py
  fi
  ##AM01 #AlphaSense CO2
  if((`echo $devbyid | grep AM01 | wc -l`>0))
  then
    echo $dev" is AlphaSense CO2"
    datalogger=./datalogger_CO2.py
  fi
  ##A9021 #WaspMote
  if((`echo $devbyid | grep A9021 | wc -l`>0))
  then
    echo $dev" is WaspMote"
    datalogger=./datalogger_wasp.py
  fi
  ##A?00 #MX3cK/ADC
  if((`echo $devbyid | grep A.00 | wc -l`>0))
  then
    echo $dev" is PC2A,MX3cK/ADC"
    datalogger=./datalogger_ADC_3.py
  fi
  #start datalogger
  echo 'start logging '$dev'.'
  nohup $datalogger --device $dev &
  sleep 1
  echo
done

#wait
sleep 2

#check
ps aux | grep '.py' | grep datalogger --color

exit

ls -lah /dev/serial/by-id/usb-*
