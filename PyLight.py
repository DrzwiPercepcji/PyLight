#!/usr/bin/python -W ignore::DeprecationWarning
import os
import sys
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

from statistics import median

#Settings:
screenW = 1920
screenH = 1080
step = 40

#Starting App.
print("PyLight started.")

stepX = screenW / step
stepY = screenH / step
step2 = step * step

rl, gl, bl = 0, 0, 0

x, y, i = 0, 0, 0

ra, ga, ba = [], [], []

temp = []
array = []
rgb = []

pixbuf = None
window = None

output = None
R, G, B = None, None, None

pixbuf = GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB, False, 8, 1, 1)

while True:
    
    array = []
    
    ra, ga, ba = [], [], []
    
    window = Gdk.get_default_root_window()
    
    x = 0
    
    while x < step:
        
        y = 0
        
        while y < step:
            
            pixbuf = Gdk.pixbuf_get_from_window(window, x * stepX, y * stepY, 1, 1)
            
            temp = pixbuf.get_pixels()
            
            ra.append(temp[0])
            ga.append(temp[1])
            ba.append(temp[2])
            
            y += 1
        
        x += 1
        
        rl = int(round((rl + median(ra)) / 2.0))
        gl = int(round((gl + median(ga)) / 2.0))
        bl = int(round((bl + median(ba)) / 2.0))
        
        rgb = [rl, gl, bl]
        
		#Output for rivalcfg command.
        '''
        output = ''.join('{:02x}'.format(c) for c in rgb)
		os.system("rivalcfg -c " + output)
        '''
		
		#Output for msi-rgb command.
        '''
        R = format(int(round(rgb[0] / 255.0 * 15.0)), 'x')
        G = format(int(round(rgb[1] / 255.0 * 15.0)), 'x')
        B = format(int(round(rgb[2] / 255.0 * 15.0)), 'x')
        os.system("sudo msi-rgb " + R + R + R + R + R + R + R + R + " " + G + G + G + G + G + G + G + G + " " + B + B + B + B + B + B + B + B)
        '''
        
        print(rgb)
        
        time.sleep(0.1)

print("PyLight exited.")