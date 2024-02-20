import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir/mam")
            return "None"
        return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    minute = time[14:16]
    speak("The time is " + hour + " Hours and " + minute + " Minutes")

def Hello():
    speak("hello sir I am your desktop assistant. Tell me how may I help you")

def Take_query():
    Hello()
    while True:
        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks")
            webbrowser.open("https://www.geeksforgeeks.org")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "which day it is" in query:
            tellDay()
        elif "tell me the time" in query:
            tellTime()
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            break
        elif "from wikipedia" in query:
            speak("Checking Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am Jack. Your desktop Assistant")

if __name__ == '__main__':
    Take_query()





