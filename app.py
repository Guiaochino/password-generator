# A Password Generator using Python

# This allows the user to generate a password composed of numbers 
# and letter that is limited to 8 chaacters

import tkinter as tk
import random
import pyperclip
from tkinter.constants import BOTTOM, CENTER, E, LEFT, NUMERIC, RIGHT, TOP, W, X

def specified_length(length):
    index = random.randrange(length)
    return index

def copy_content():
    pyperclip.copy(passText['text'])
    pass

def generatePass():
    numList = [num for num in range(10)]
    charList = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    password = ''
    
    while len(password) < 8:

        numlet = random.randrange(2)

        if numlet == 0:
            i = specified_length(len(numList))
            password += str(numList[i])
        elif numlet == 1:
            i = specified_length(len(charList))
            password += charList[i]
        
    passText['text'] = password


app = tk.Tk()
app.title('Password Generator')
app.geometry('640x240')
app.configure(bg='#333333')

copyImage = tk.PhotoImage(file='copy.png')
resizeImage = copyImage.subsample(15, 15)

titleText = tk.Label(
    app,
    text='Password Generator',
    bg='#333333',
    fg='#DFDFDF',
    font=('arial', 24, 'bold')
)

passText = tk.Label(
    app,
    bg='#DFDFDF',
    bd=None,
    font=('arial', 16),
    width=30,
    justify=LEFT,
    text= '',
    padx=15
)

frame01 = tk.Frame(
    app,
    bg='#333333',
    padx=50
)

btnGenerate = tk.Button(
    frame01,
    activebackground='#666666',
    activeforeground='#DFDFDF',
    bd=None,
    bg='#DFDFDF',
    fg='#333333',
    text='Generate\nPassword',
    justify=CENTER,
    width=20,
    height= 2,
    padx=5,
    command=generatePass
)

copybutton = tk.Button(
    frame01,
    activebackground='#333333',
    bg='#DFDFDF',
    bd=None,
    image=resizeImage,
    padx=2,
    pady=2,
    command=copy_content
)

authorText = tk.Label(
    app,
    bg='#333333',
    fg='#DFDFDF',
    bd=None,
    font=('arial', 8),
    justify=CENTER,
    text='Author: Guiaochino Miguel G. Tiamzon'
)



app.update()
authorText.pack(side=BOTTOM)
copybutton.pack(side=RIGHT)
btnGenerate.pack(side=LEFT)
frame01.pack(side=BOTTOM, fill=X)
passText.pack(side=BOTTOM, expand=True)
titleText.pack(side=TOP, fill=X)
app.mainloop()