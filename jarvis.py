import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=datetime.datetime.now().hour
    if 0<=hour<12:
        speak("good morning sir")
    elif 12<=hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("hello sir i am jarvis . tell me how may i help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said : {query}")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query
if __name__=="__main__":
    wishme()
    while(True):
        query=takecommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("searching wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            webbrowser.open("https://www.bing.com/videos/search?q=295+song&view=detail&mid=B5CECBD9059FA304B73BB5CECBD9059FA304B73B&FORM=VIRE")
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")
        elif "open code" in query:
            codpath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codpath)
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "open twitter" in query:
            webbrowser.open("twitter.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "bye jarvis" in query:
            speak("bye sir will meet you tomorrow")
            quit()