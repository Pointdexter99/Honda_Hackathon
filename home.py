from tkinter import *
import pyttsx3
# import Jarvis
import consolelog
from PIL import ImageTk,Image

root = Tk()




def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello World ")
    engine.runAndWait()



word = Label(root, text="Honda Assistant DashBoard Prototype", font="Times 40 bold", pady=20)
word.grid(row = 1, column = 2)

mic = PhotoImage(file = 'mic.PNG')

micButton = Button(root,image= mic,height = 100,width = 53 , border =0 )

micButton.grid(row = 2, column = 2)

mapheading= Label(root,text="Your Current Location",font = "Times 20 bold",padx=20)
mapheading.grid(row=4,column=1)

logo = ImageTk.PhotoImage(Image.open("Honda.JPG"))
mylogo = Label(image = logo ,pady = 20)
mylogo.grid(row = 3 , column = 2)

map_image = ImageTk.PhotoImage(Image.open("map.JPEG"))
mylabel = Label(image=map_image,padx= 20)
mylabel.grid(row = 5,column = 1)


histheading = Label(root , text = "Your Usage Stats" , font = "Times 20 bold")
histheading.grid(row=4,column = 3)


hist = ImageTk.PhotoImage(Image.open("hist.PNG"))
myhist = Label(image = hist  )
myhist.grid(row = 5, column=3)





root.mainloop()












