import pyttsx3
import datetime 
import webbrowser
import speech_recognition as sr
import smtplib
 
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Boss . Please tell me how may I help you")
def interact():
    speak('I can send email to your friends,  show you your location,  detect potholes in your roadway, locate nearby hospitals for you,   show you your location,  or call nine one one if you are in danger. What would you like me to do..??')
   

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source) 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        speak("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

 
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.  


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sumonbhattacharjee599@gmail.com', 'sumon123')
    server.sendmail('sumonbhattacharjee599@gmail.com', to, content)
    server.close()

if __name__=="__main__" :
    wishme()
    m=True
    while m==True:
        q = takeCommand().lower()

        if 'do for me' in q:
            interact()
            query = takeCommand().lower()
            if 'help' in query:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'medical' in query:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'health' in query:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'sos' in query:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'potholes' in query:
                speak('Searching for potholes in the area..')
                webbrowser.open("https://www.google.com/maps/")
                print('Searching for potholes in the area..')
            if 'locate my position' in query:
                speak('Locating your position')
                webbrowser.open("https://www.google.com/maps/")
            if 'girlfriend' in query:
                speak('I am looking for your girlfriend')
                webbrowser.open("https://www.instagram.com/sucharita1997/")
            if 'thanks' in query:
                speak('I will be right here if you need something else')
                print("Thank you.!!")
                m=False
            elif  'friend' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "tanmoybanerjeetvf@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")
        else:
            if 'help' in q:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'medical' in q:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'health' in q:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'sos' in q:
                speak('Searching for nearby medical health support..')
                webbrowser.open("https://www.google.com/maps/search/Hospitals/")
                print('Searching for nearby medical health support..')
            if 'potholes' in q:
                speak('Searching for potholes in the area..')
                webbrowser.open("https://www.google.com/maps/")
                print('Searching for potholes in the area..')
            if 'locate my position' in q:
                speak('Locating your position')
                webbrowser.open("https://www.google.com/maps/")
            if 'thanks' in q:
                speak('I will be right here if you need something else')
                print("Thank you.!!")
                m=False
            elif  'email my friend' in q:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "tanmoybanerjeetvf@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")




 