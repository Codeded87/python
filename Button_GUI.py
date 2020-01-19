# !/usr/bin/python3  
from tkinter import *  
#creating the application main window.   
parent = Tk()  
redbutton = Button(parent, text = "RED", fg = "red")
redbutton.pack(side = LEFT)

greebutton = Button(parent, text="green", fg = "green")
greebutton.pack(side = RIGHT )

bluebutton = Button(parent, text = "blue", fg = "blue")
bluebutton.pack(side = TOP)

blackbutton = Button(parent, text = "black", fg = "black")
blackbutton.pack(side = BOTTOM)

#Entering the event main loop  
parent.mainloop() 
