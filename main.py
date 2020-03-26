# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:08:39 2020

@author: C.-C. Wang
"""
# import all needed package
from tkinter import Tk, Label, Button, StringVar
from random import choice
# build the ascii code list
random_list = []
def build_random_list(a, b, lst):
    for i in range(a, b+1):
        lst.append(i)
    return lst
random_list = build_random_list(48, 57, random_list)
random_list = build_random_list(65, 90, random_list)
random_list = build_random_list(97, 122, random_list)
# Create the random passward (default size = 12)
def create_random_passward(length=12):
    lst = ''
    for i in range(length):
        lst += chr(choice(random_list))
    return lst
passward = create_random_passward()    
# The width and height of the GUI
width = 300
height = 75
# The environmnet setting
window = Tk()
window.title('Random Passward')
window.geometry(str(width)+"x"+str(height)+"+480+270")
window.resizable(False, False)
# The label that show the passward
var = StringVar()
show_label = Label(window,
            textvariable=var, 
            bg='white', 
            font=('Arial',12), 
            width=50, height=1)
show_label.pack()
# The instruction label
text_label = Label(window,
            text='Passward Length',
            #bg='white',
            font=('Arial',12),
            width=30, height=1)
text_label.pack()
# The button that create the passwards in length of 8, 10, 15, 20
def show_passward_8():
    var.set(create_random_passward(8))
show_passward_button_8 = Button(window, text='8', width=8, height=1, command=show_passward_8)
show_passward_button_8.place(x=5,y=48,anchor='nw')
def show_passward_10():
    var.set(create_random_passward(10))
show_passward_button_10 = Button(window, text='10', width=8, height=1, command=show_passward_10)
show_passward_button_10.place(x=width*0.25+5,y=48,anchor='nw')
def show_passward_15():
    var.set(create_random_passward(15))
show_passward_button_15 = Button(window, text='15', width=8, height=1, command=show_passward_15)
show_passward_button_15.place(x=width*0.5+5,y=48,anchor='nw')
def show_passward_20():
    var.set(create_random_passward(20))
show_passward_button_20 = Button(window, text='20', width=8, height=1, command=show_passward_20)
show_passward_button_20.place(x=width*0.75+5,y=48,anchor='nw')
# Run the program
window.mainloop()