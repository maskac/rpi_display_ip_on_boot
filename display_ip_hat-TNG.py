#!/usr/bin/python3

import socket
from sense_hat import SenseHat

sense = SenseHat()
scroll_speed = 0.1
color = (0,255,0)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def rotate():
    x = round(sense.get_accelerometer_raw()["x"],0)
    y = round(sense.get_accelerometer_raw()["y"],0)
    rot = 0
    if x == -1:
        rot = 90
    elif y == -1:
        rot = 180
    elif x==1:
        rot=270
    sense.set_rotation(rot)

rotate()
ip = get_ip()
#print(ip)

sense.show_message(ip, scroll_speed, color)
