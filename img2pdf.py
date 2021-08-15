import os
from PIL import Image

def img2pdf(filename,path=os.getcwd()):
    os.chdir(path)
    img_list=[]
    file_list=[]
    for file in os.listdir():
        if file.endswith('.jpg' or '.png'):
            file=file.split('.')[0]
            file_list.append(file)    
    for x in file_list:
        img = Image.open(x+'.jpg')
        img_list.append(img)
    im1=img_list[0]
    im1.save(filename+".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_list[1:])
