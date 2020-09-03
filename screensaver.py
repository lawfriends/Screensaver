# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:51:39 2020

@author: lawfr
"""

from PIL import Image, ImageColor
import random
import ctypes

width = 1920
height = 1080

section_number = random.randint(3, 16)

ss = Image.new('RGB', (width,height), 'white')

ss.save("screensaver.bmp")

#box=120

#while ((width%box!=0 or height%box!=0) and box<height/4):
#    box=box+1

box_x = width//section_number
box_y = height//section_number

R = (random.randint(0,255), random.randint(0,255))
G = (random.randint(0,255), random.randint(0,255))
B = (random.randint(0,255), random.randint(0,255))


for i in range(0,section_number//2+section_number%2):
    for j in range(0, section_number):
        if random.randint(0,1)==0:
            index = random.randint(0,1)
            R_c = R[index]
            G_c = G[index]
            B_c = B[index]
        else:
            R_c = 255
            G_c = 255
            B_c = 255
        for x in range(i*box_x, (i+1)*box_x):
            for y in range(j*box_y, (j+1)*box_y):
                ss.putpixel((x, y), (R_c, G_c, B_c))

for i in range(section_number//2+section_number%2, section_number):
    for j in range(0, section_number):
        for x in range(i*box_x, (i+1)*box_x):
            for y in range(j*box_y, (j+1)*box_y):
                R_c, G_c, B_c = ss.getpixel(((section_number-1-i)*box_x, j*box_y))
                ss.putpixel((x, y), (R_c, G_c, B_c))
                
ss.save("screensaver.bmp")
try:
    ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:\\Users\\lawfr\\DDocuments\\Progetti\\Screensaver\\screensaver.bmp" , 0)
except:
    print("Errore")
                