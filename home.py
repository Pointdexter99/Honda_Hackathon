from tkinter import *
import pyttsx3
import Jarvis
import consolelog
from PIL import ImageTK,Image


root = Tk()




def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello World ")
    engine.runAndWait()



word = Label(root, text="Honda Assistant DashBoard Demo", font="Times 40 bold", pady=20)
word.pack()

mic = PhotoImage(file = 'mic.PNG')

micButton = Button(root,image= mic,height = 100,width = 53 , border =0 ,command=Jarvis.intro)

micButton.pack()

map_image = ImageTK.PhotoImage(Image.open("map.PNG"))
mylabel = Label(image=map_image)
mylabel.pack(side = LEFT)






root.mainloop()












