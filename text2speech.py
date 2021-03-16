import os
from tkinter import *

from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x300")
root.config(bg='ghost white')
root.title("Text2Speech")
Label(root, text="Text2Speech", font="arial 20 bold", bg='white smoke').pack()
Msg = StringVar()
Label(root, text="Enter text", font='arial 15 bold', bg='white smoke').place(x=20, y=60)
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


def Text_to_Speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save('speech.mp3')
    playsound('speech.mp3')
    os.remove("speech.mp3")


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


Button(root, text="PLAY", font='arial 15 bold', command=Text_to_Speech, width='4').place(x=25, y=140)

Button(root, font='arial 15 bold', text='EXIT', width='4', command=Exit, bg='OrangeRed1').place(x=100, y=140)

Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset).place(x=175, y=140)

root.mainloop()
