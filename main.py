from tkinter import *
from pygame import mixer


root = Tk()
root.title("Kenner Player")
root.iconbitmap(r'logo.ico')
root.geometry('640x480')

text = Label(root, text = 'The lightest player!')
text.pack()

photo = PhotoImage(file='play32.png')
#labelphoto = Label(root,image = photo)
#labelphoto.pack()
def play_btn():
    print("button working")

btn = Button(root, image=photo, command = play_btn)
btn.pack()

root.mainloop()