import pyttsx3
import wikipedia
import datetime
import os
import webbrowser

import smtplib

from tkinter import *
from PIL import ImageTk, Image
print("INITIALIZING JARVIS....")

master = "SAKSHAM SIR"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme(): 
    hour=int(datetime.datetime.now().hour)
    
    
    if hour>=0 and hour<12:
        speak("Good morning" +master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +master)
    else:
        speak("Good Evening" +master)        

def takecommmand():


    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)

    try:
        print("Recognizing......") 
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Say that again please")
        query= None
    return query
 


class Widget:
    def __init__(self):
       root = Tk()
       root.title('Jarvis(Mark-1)')
       root.config(background='Red')
       root.geometry('1280x720')
       root.resizable(0, 0)
       img = ImageTk.PhotoImage(Image.open(r"D:\man1.png"))
       panel = Label(root, image = img)
       panel.pack(side='right', fill='both',expand = "no")

       

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Run Jarvis\' to Give commands')

       userFrame = LabelFrame(root, text="User", font=('Black ops one',10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
       left2.config(font=("Century Gothic", 24, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="Jarvis", font=('Black ops one',10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#3B3B98',fg='white')
       left1.config(font=("Century Gothic", 24, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Run Jarvis', font=('Black ops one', 10, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')

       
       
       self.compText.set('Hello, I am Jarvis! What can i do for you Sir ??')

       root.bind("<Return>",self.clicked) # handle the enter key event of your keyboard
       root.mainloop()

    def clicked(self):
        print('Working')
        query = takecommmand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
       
        if 'wikipedia'in query:
            speak("Searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube")  
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open facebook' in query.lower():
            speak("opening facebook")  
            url = "facebook.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)  

        elif 'open instagram' in query.lower():
            speak("opening instagram")  
            url = "instagram.com" 
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open gmail' in query.lower():
            speak("opening g-mail")  
            url = "gmail.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open flipkart' in query.lower():
            speak("opening flipkart")  
            url = "flipkart.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query.lower():
            speak("Alright sir playing music")
            songs_dir="D:\\music\\songs" 
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'play videos' in query.lower():
            speak("Alright here's some entertainment for you sir")
            video_dir="D:\\video"
            videos=os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))

        elif 'show college festival photos' in query.lower():
            speak("Alright here's you go sir")
            image_dir="D:\\DSLR\\techno\\Canon"
            images=os.listdir(image_dir)
            os.startfile(os.path.join(image_dir,images[16]))

        elif 'thank you' in query.lower():
            speak("Its my pleasure sir to always help you")


        elif 'sorry' in query.lower():
            speak("well if you really are then say it to my master") 

        elif 'please' in query.lower():
            speak("Don't say please sir!!!... I'm always here to help you")

        elif 'ek hi nara ek hi naam' in query.lower():
            speak("jay shree raam, jay shree raam")  

        elif 'bolo har har mahadev' in query.lower():
            speak("har har mahadev")     
                
        elif 'what can you do' in query.lower():
            speak("its better if you ask what kind of assistant you are")

        elif'what kind of assistant are you' in query.lower():
            speak("kind of helpful")

        elif'help me'in query.lower():
            speak("always ready to help you saksham sir")

        elif 'what is your name' in query.lower():
            speak("jarvis sir")
            
        elif 'who made you' in query.lower():
            speak("saksham sir")

        elif 'ok google' in query.lower():
            speak("thats not me sir....i am jarvis")

        elif 'hey siri' in query.lower():
            speak("i am jarvis sir,how can you forget something which is created by you sir") 

        elif 'i want to be rich' in query.lower():
            speak("so do i") 

        elif 'sing me a song' in query.lower():
            speak("Alright sir! i will try for you")
            songs_dir="D:\\music\\songs" 
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[30]))  

        elif 'can you laugh' in query.lower():
            speak("well if you really want so")
            playsound('D:/project/jarvis/audio/laugh.mp3')  

        elif 'tell me joke ' in query.lower():
            speak("Sir i am not good in scarsam as you were")
    


if __name__ == '__main__':
    speak("INITIALIZING JARVIS")
    wishme()
    widget = Widget()  

   