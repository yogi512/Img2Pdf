

import tkinter as tk
import os
r = tk.Tk()
r.title('Img to Pdf ')
def click():
    file_list.append(file)
    print(file_list)
    label = tk.Label(r,text=file)
    label.pack()

file_list=[]    
def place():
    pass

i=1
for file in os.listdir():
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        file=file.split('.')[0]
        button= tk.Button(r, text=file)
        button.pack()  

submit = tk.Button(r,text='GENERATE PDF',command=quit)
submit.pack()
r.mainloop()


