"""
motion detector tool based in pixels differences from diff frames
"""


from PIL import Image
from os.path import join
import numpy as np
import os

frames_dir = "/home/pi/results/frames_from_video"

frames = os.listdir(frames_dir)

im = Image.open(join(frames_dir,"frame0.jpg"))
red0, green, blue = im.split()
red0_np = np.array(red0, dtype='float')
im = Image.open(join(frames_dir,"frame1.jpg"))
red1, green, blue = im.split()
red1_np = np.array(red1, dtype='float')

dif = np.abs(red0_np-red1_np)
np.mean(dif)

import re

def get_numbers(texto):
    return int(re.findall(r'[0-9]+', texto)[0])

def sort_list(l):
    dicto = {}
    for i in l:
        dicto[get_numbers(i)] = i
    lista = []
    for i in sorted(list(dicto.keys())):
        lista.append(dicto[i])
    return lista


frames = sort_list(frames)

print('frames: ', frames[:30])

movement = []
for f in frames:
    im = Image.open(join(frames_dir,f))
    red, green, blue = im.split()
    red_np = np.array(red, dtype='float')
    if "red_old" in locals():
        dif = np.mean(np.abs(red_old-red_np))
        if dif>3.5:
            movement.append(f)
        red_old = red_np
    else:
        red_old = red_np
print("\nMovement: ", movement)
