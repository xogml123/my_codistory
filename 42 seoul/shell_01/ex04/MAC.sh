#!/bin/sh

ifconfig -a | grep -ioE '([a-z0-9]{2}:){5}..'
ifconfig -a link | grep ether | cut -d ' ' -f 2
