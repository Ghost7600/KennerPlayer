from tkinter import *
from pygame import mixer

mixer.init() # init mixer


root = Tk() #creates windows obj
root.title("Kenner Player")
root.iconbitmap(r'logo.ico')
root.geometry('640x480')
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