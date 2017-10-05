#!/usr/bin/python

import socket
import fcntl
import struct
from sense_hat import SenseHat

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
sense = SenseHat()

ip = get_ip_address('wlan0')  # '192.168.0.110'

sense.show_message(ip, scroll_speed=0.1, text_colour=[255,0,0], back_colour=[0,0,0])

sense.clear()
