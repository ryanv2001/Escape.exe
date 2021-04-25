from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import ttk
import tkinter as tk
import turtle
import random
import time
import PIL
from PIL import ImageTk, Image


#-------------------------------------------------------------------#
root = tk.Tk()
root.title('400 Meter Dash')
root.geometry('1130x700')
root.config(bg='black')
#-------------------------------------------------------------------#


#-------------------------------------------------------------------#
bg_image = PhotoImage(file = 'RunTrack.png')
lbl = tk.Label(root, image=bg_image)
lbl.img = bg_image  
lbl.place(relx=0.5, rely=0.5, anchor='center')
#-------------------------------------------------------------------#

ft1 = 'cambria 15 bold'
ft2 = 'times 15'

#-------------------------------------------------------------------#
def Objective_Instructions():
    ObjLabel = tk.Label(root, text='Objective')
    ObjLabel.config(font=ft1, width=20, 
        relief='raised', borderwidth=2, fg='black')
    ObjLabel.place(x=550,y=100, anchor='center')

    ObjButton = tk.Button(ObjLabel, text='Beat the CPU to the Finish Line!')
    ObjButton.config(font=ft2)

    Instruc_Label = tk.Label(root, text='Instructions')
    Instruc_Label.config(font=("Cambria", 15), height=50, width=50)
    Instruc_Label.place(x=550, y=500, anchor='center')
   
    Instructions = """There is an automatic standard die (1-6) that rolls once per turn. Your runner will  move foward the number that is rolled times 100 pixels. If you land above a 4, you   will be prompted a challenge question. Get it RIGHT and you continue. Get it WRONG   and you move backwards 100 pixels."""
    T = Text(Instruc_Label, height=4, width=85)
    T.insert(tk.END, Instructions)
    T.pack()

Objective_Instructions()
#-------------------------------------------------------------------#
def start():
    start = Button(root, text="Start")#, command=)
    start.place(x=50, y=600)
start()
#-------------------------------------------------------------------#

def exit():
    exit = Button(root, text= "Exit", command = root.destroy)
    exit.place(x=1000, y=600)
exit()
#-------------------------------------------------------------------#
def PlaceHolders():
    #(0,0)
    PlaceHolderLabel1 = tk.Label(root, text='|', fg='red')
    PlaceHolderLabel1.place(x=0,y=0)
    #(0,500)
    PlaceHolderLabel2 = tk.Label(root, text='|', fg='red')
    PlaceHolderLabel2.place(x=1120,y=0)
    #(1000,500)
    PlaceHolderLabel3 = tk.Label(root, text='|', fg='red')
    PlaceHolderLabel3.place(x=1120, y=600)

    PlaceHolderLabel4 = tk.Label(root, text='|', fg='red')
    PlaceHolderLabel4.place(x=0, y=680)

    PlaceHolderLabel5 = tk.Label(root, text='|', fg='red')
    PlaceHolderLabel5.place(x=550, y=60)
PlaceHolders()

#-------------------------------------------------------------------#
root.mainloop()
