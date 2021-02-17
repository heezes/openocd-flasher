#!/bin/bash

sudo openocd -s openocd-spi/tcl \
	-f openocd.cfg	\
	-f flash.ocd
