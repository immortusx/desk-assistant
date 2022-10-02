import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-us')
            command = command.lower()
            if 'boys' in command:
                print(command)
            else:
                hour = datetime.datetime.now().hour
                if hour >= 22 and hour < 6:
                    speak('Good Night Sir, Take care ')
                    print('Good Night Sir, Take care ')

    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
    return command

def run_boys():
    command = get_command()
    if 'play' in command:
        song =command.replace('play', '')
        speak('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        speak('The Current time is' + time)
        print(time)
    elif 'who is the' in command:
        person = command.replace('who is the', '')
        info = wikipedia.summary(person, 1)
        speak(info)
        print(info)
    elif 'jokes' in command:
        speak(pyjokes.get_joke())
    elif 'youtube' in command:
        video = command.replace('play', '')
        speak(('Playing video on Youtube' + video))
        pywhatkit.playonyt(video)

run_boys()

def greet_user():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Morning, Sir')
        print('Good Morning, Sir')
    elif hour >= 12 and hour < 16:
        speak('Good Afternoon, Sir')
        print('Good Afternoon, Sir')
    elif hour >= 16 and hour < 22:
        speak('Good Evening, Sir')
        speak('I am Boys, How may I assist you')
        print('Good Evening, Sir')

greet_user()