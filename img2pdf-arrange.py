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
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        print(file)
print("Choose the files in order without extension")
print("Leave blank and press enter to stop")
while True:
    file = input()
    if file!='':
        if file+'.jpg' in os.listdir():
            file_list.append(file+'.jpg')
        elif file+'.jpeg' in os.listdir():
            file_list.append(file+'.jpeg')
        elif file+'.png' in os.listdir():
            file_list.append(file+'.png')
        else:
            print('FileNameMismatch')
    else :
        break
file_list  
for x in file_list:
    img = Image.open(x)
    img_list.append(img)
im1=img_list[0]
im1.save(FILENAME+".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_list[1:])
