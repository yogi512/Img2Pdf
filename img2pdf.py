#!/usr/bin/python3
import os
import sys
from PIL import Image

FILENAME=str(sys.argv[1])
ORG_HEAD=str(sys.argv[2])

os.chdir(ORG_HEAD)
img_list=[]
file_list=[]
for file in os.listdir():
    if file.endswith('.jpg' or '.png'):
        file=file.split('.')[0]
        file_list.append(file)    
file_list.sort()
for x in file_list:
    img = Image.open(x+'.jpg')
    img_list.append(img)
im1=img_list[0]
im1.save(FILENAME+".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_list[1:])
