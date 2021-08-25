#!/usr/bin/python3
import os
import sys
import getopt
from PIL import Image

argv = sys.argv[1:]

VERBOSE =" imgs2pdf [-a or -- arrange ] FILENAME DIRECTORY to  arrange images manually \n imgs2pdf [-t or -- time ] FILENAME DIRECTORY to  arrange images based on time modified \n "
ERROR ='try using imgs2pdf FILENAME DIRECTORY \nimgs2pdf -h  or imgs2pdf --help for more details'       

try:
    opts,args= getopt.getopt(argv, "a:t:h",["arrange=","time=","help"]) # in short form ':' represent that the option takes an argument
except:                                                                 # in long form '=' represent that the option takes an argument
    print("Error")

if opts==[]:
    try :
        FILENAME = sys.argv[1]
        DIRECTORY = sys.argv[2]
        os.chdir(DIRECTORY)
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
    except:
        print(ERROR)
else:
    for opt, arg in opts:
        if opt in ['-a','--arrange']:
            FILENAME = arg
            DIRECTORY = args[0]
            os.chdir(DIRECTORY)
            img_list=[]
            file_list=[]

            for file in os.listdir():
                if file.endswith('.jpg'):
                    print(file)
            print("Choose the files in order without extension")
            print("Leave blank and press enter to stop")
            while True:
                file = input()
                if file != '':
                    file_list.append(str(file))
                else :
                    break
            file_list  
            for x in file_list:
                img = Image.open(x+'.jpg')
                img_list.append(img)
            im1=img_list[0]
            im1.save(FILENAME+".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_list[1:])


        elif opt in ['-t','--time']:

            FILENAME=arg
            DIRECTORY = args[0]
            os.chdir(DIRECTORY)

            img_list=[]
            file_list=[]
            for file in os.listdir():
                if file.endswith('.jpg' or '.png'):
                    file_list.append(file)
            sorted(file_list, key=lambda t: os.stat(t).st_mtime)
            file_list = list(map(lambda x:x.split('.')[0],file_list))
            for x in file_list:
                img = Image.open(x+'.jpg')
                img_list.append(img)
            im1=img_list[0]
            im1.save(FILENAME+".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_list[1:])

        elif opt in ['-h','--help']:

            print(VERBOSE)


    