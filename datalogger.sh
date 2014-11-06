#!/bin/bash

nohup ./datalogger.py --device /dev/ttyUSB0 &
nohup ./datalogger.py --device /dev/ttyUSB1 &
