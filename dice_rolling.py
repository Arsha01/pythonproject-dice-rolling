import tkinter
from PIL import Image, ImageTk
import random

box = tkinter.Tk()
box.geometry('400x400')
box.title('Roll The Dice')

blankline= tkinter.Label(box,text='')
blankline.pack()

headingline= tkinter.Label(box,text='Hello There!',bg='white',fg='blue',font='Helvetica 16 bold italic')
headingline.pack()

dice = ['die1.PNG','die2.PNG','die3.PNG','die4.PNG','die5.PNG','die6.PNG']

currentimage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

imagelabel = tkinter.Label(box,image=currentimage)
imagelabel.image=currentimage
imagelabel.pack(expand=True)

def rolling_dice():
    currentimage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    imagelabel.configure(image=currentimage)
    imagelabel.image = currentimage

button = tkinter.Button(box,text='Roll The Dice',fg='red',command=rolling_dice)
button.pack(expand=True)

box.mainloop()

