#!/bin/bash

thermal_reading=$(tail -1 /sys/bus/w1/devices/*/w1_slave | cut -d'=' -f2)
celsius=$(echo "scale=2; $thermal_reading*.001" | bc)
fahrenheit=$(echo "scale=2;((9/5) * $celsius) + 32" |bc)

zabbix_sender -z {{ zabbix_server }} -s '{{ inventory_hostname }}' -k temperature.celsius -o $celsius
zabbix_sender -z {{ zabbix_server }} -s '{{ inventory_hostname }}' -k temperature.fahrenheit -o $fahrenheit
