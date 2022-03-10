import datetime
import imp
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess as sp
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

def open_notepad():
    os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
   
    wishMe()
    speak("I am your virtual assistant. You don't need to type anything. Just ask something and  I will try my best to help you out.")
    speak("You can about any famous personality by telling their name, i can open few common sites for you, play music for you, you can ask the time, i can even send mail on your behalf. Isn't that wonderful and exciting?")

    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'camera' in query:
             sp.run('start microsoft.windows.camera:', shell=True)

        elif 'open command promt' in query:
             os.system('start cmd')
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video =takeCommand()
            kit.playonyt(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand()
            kit.search(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand()
            kit.sendwhatmsg_instantly(f"+91{number}", message)
            speak("I've sent the message sir.")

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to ishani' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ishudey11032002@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ishu. I am not able to send this email")  
        elif 'quit' in query:
            speak("thankyou.always for your help")
            break          


