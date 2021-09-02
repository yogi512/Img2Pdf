import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
from PIL import Image
import sys

# create the root window
root = tk.Tk()
root.geometry('300x300')
# root.resizable(False, False)
root.title('Image to Pdf')
file_list=[]
new_list=[]
img_list=[]
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
FILENAME = sys.argv[1]




for file in os.listdir():
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        file=file.split('.')[0]
        file_list.append(file)


langs_var = tk.StringVar(value=file_list)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    selectmode='extended',
    font='Montserrat',
    disabledforeground='#12f313',
    highlightcolor='black',
    selectbackground='#34d2eb')

# listbox.grid(
#     column=0,
#     row=0,
#     sticky='nwes'
# )

listbox.pack(padx=5, pady=10)

# handle event
def items_selected(event):
    """ handle item selected event
    """
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    for i in selected_indices:
    #     new_list.append(listbox.get(i))
    # for file in new_list:

        # if file+'.jpg' in os.listdir():
        #     img_list.append(Image.open(file+'.jpg'))
        # elif file+'.jpeg' in os.listdir():
        #     img_list.append(Image.open(file+'.jpeg'))
        # elif file+'.png' in os.listdir():
        #     img_list.append(Image.open(file+'.png'))
        # else:
        #     pass
        file=listbox.get(i)
        if file+'.jpg' in os.listdir():
            img_list.append(Image.open(file+'.jpg'))
        elif file+'.jpeg' in os.listdir():
            img_list.append(Image.open(file+'.jpeg'))
        elif file+'.png' in os.listdir():
            img_list.append(Image.open(file+'.png'))
        else:
            pass
    img1=img_list[0]
    img1.save(FILENAME+".pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_list[1:])
    
    
    # print(new_list)
    

listbox.bind('<<ListboxSelect>>', items_selected)



# var=tk.StringVar(value=new_list)

for val in new_list:
    label = tk.Label(root,text=val)
    label.pack()

button = tk.Button(root,text='GENERATE PDF',font='Montserrat-Bold',activebackground='#34d2eb',command=quit)
button.pack(side='bottom',pady=10)



root.mainloop()
