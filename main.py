from tkinter import *
from pygame import mixer

mixer.init() # init mixer


root = Tk() #creates windows obj
root.title("Kenner Player")
root.iconbitmap(r'logo.ico')
root.geometry('640x480')

#creating menubar
menubar = Menu(root)
root.config(menu = menubar) #makiing it stick to the top and preparing for submenus


#creating submenus
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open")
submenu.add_command(label="Exit")

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About")




mixer.music.load("Matt_Oakley-Mercury_Ascendant.mp3")

text = Label(root, text = 'The lightest player!')
text.pack()


#labelphoto = Label(root,image = photo)
#labelphoto.pack()
def playsong():
    mixer.music.play()
    print("playing song")

def pausesong():
    mixer.music.pause()

def setvol(val):
    vol= int (val)/100
    mixer.music.set_volume(vol)

playphoto = PhotoImage(file='play32.png')
playbtn = Button(root, image=playphoto, command = playsong)
playbtn.pack()

stopbtn=Button(root,text='PAUSE',command = pausesong)
stopbtn.pack()

scale = Scale(root,from_=0,to=100,orient=HORIZONTAL,command= setvol)
scale.set(10)
scale.pack()



root.mainloop()