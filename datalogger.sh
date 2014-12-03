#!/bin/bash

#launch WaspMote (FTDI_FT232R_USB_UART_A9021)
for dev in /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9021*
do
  echo 'start logging WaspMote from '$dev
  dev=/dev/ttyUSB`ls -lah $dev | tail -c 2 | head -c 1`
  nohup ./datalogger.py --device $dev &
  sleep 1
done

#launch NDIR-CO2 (FTDI_FT232R_USB_UART_AM01V)
for dev in /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AM01V*
do
  echo 'start logging NDIR-CO2 from'$dev
  dev=/dev/ttyUSB`ls -lah $dev | tail -c 2 | head -c 1`
  nohup ./datalogger_CO2.py --device $dev &
  sleep 1
done

#wait
sleep 2

#check
ps aux | grep datalogger --color
