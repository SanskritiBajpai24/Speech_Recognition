import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os

# Initialize engine globally
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal Assistant. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.")
        return "None"
    return query

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().strftime("%B")
    day = datetime.datetime.now().day
    speak(f"Today's date is {day} {month} {year}")

def main():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("Multiple results found. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, no information found.")

        elif 'open' in query:
            if 'google' in query:
                webbrowser.open("http://www.google.com")
            elif 'youtube' in query:
                webbrowser.open("http://www.youtube.com")
            elif 'instagram' in query:
                webbrowser.open("http://www.instagram.com")
            elif 'twitter' in query:
                webbrowser.open("http://www.twitter.com")
            elif 'whatsapp' in query:
                webbrowser.open("http://web.whatsapp.com")
            elif 'drive' in query:
                drive_letter = query.split()[-1].upper()
                os.startfile(f"{drive_letter}:")

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strtime}")

        elif 'date' in query:
            date()

        elif 'shutdown' in query:
            speak("Are you sure you want to shutdown?")
            response = takeCommand().lower()
            if 'yes' in response:
                speak("Shutting down the system")
                os.system("shutdown /s /t 1")
            elif 'no' in response:
                speak("Cancelled the shutdown")

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
