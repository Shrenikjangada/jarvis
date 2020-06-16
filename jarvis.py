import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour<12):
        speak("Good Morning")
    elif(hour >=12 and hour <18):
        speak("Good Afternoon sir")
    else:
        speak("Good Evening")
    speak("I Am Jarvis. Please tell me How may i help you")

def takecommand():
    """ It Takes Microphone input from user and givves string as output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print("Say That again please")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("jangadashrenik@gmail.com", "itsme123#")
    server.sendmail("jangadashrenik@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        #Logic for executing tasks
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "how are you" in query:
            speak("I am good sir")
            speak("How Are You")
        elif "i am fine" in query:
            speak("good to hear sir")
            speak("How may i help you")
        elif "open youtube" in query:
            speak("Okay sir")
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = "E:\\Songs"
            songs = os.listdir(music_dir)
            num = random.randint(0,len(songs))
            speak("Ok sir playing music")
            os.startfile(os.path.join(music_dir,songs[num]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The time is")
            speak(strtime)
        elif 'open notepad plus' in query:
            path = "F:\\Notepad++\\notepad++.exe"
            os.startfile(path)
        elif "send email" in query:
            try:
                speak("What should i say")
                content = takecommand()
                to = "shrenikjangada788@gmail.com"
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                speak("Sorry sir i am unable to send this email")
        elif "bye" in query:
            speak("Thankyou sir for your time")
            speak("Byee")
            break