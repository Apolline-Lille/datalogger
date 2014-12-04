#!/bin/bash

#launch all datalogger for any devices reconized in /dev/serial/by-id/usb-*

#launch WaspMote (FTDI_FT232R_USB_UART_A9021)
for dev in /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9021*
do
  if [ -e $dev ]
  then
    /bin/echo -n 'start logging WaspMote from '$dev
    dev=/dev/ttyUSB`ls -lah $dev | tail -c 2 | head -c 1`
    echo ' i.e. '$dev
    nohup ./datalogger.py --device $dev &
    sleep 1
  fi
done

#launch NDIR-CO2 (FTDI_FT232R_USB_UART_AM01V)
for dev in /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AM01V*
do
  if [ -e $dev ]
  then
    /bin/echo -n 'start logging NDIR-CO2 from '$dev
    dev=/dev/ttyUSB`ls -lah $dev | tail -c 2 | head -c 1`
    echo ' i.e. '$dev
    nohup ./datalogger_CO2.py --device $dev &
    sleep 1
  fi
done

#wait
sleep 2

#check
ps aux | grep datalogger --color
