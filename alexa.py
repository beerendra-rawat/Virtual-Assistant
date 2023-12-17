import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random

listener = sr.Recognizer()
engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

#Wish function
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        talk("good morning i am virtual assistent Buddy! How May i Help you..")
    elif hour>=12 and hour<18:
        talk("good afternoon i am virtual assistent Buddy! How May i Help you..") 
    else:
        talk("good evening i am virtual assistent Buddy! How May i Help you..")
wish()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buddy' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "wikipedia" in command:
        command("searching details....Wait")
        command.replace("wikipedia","")
        results = wikipedia.summary(command,sentences=2)
        print(results)
        talk(results)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'how are you' in command:
        stMsgs = ['I am fine! and you', 'Nice! and you','i am okey and you']
        ans_q = random.choice(stMsgs)
        talk(ans_q) 

    elif 'good' in command or 'fine' in command:
        talk('ok')
        
    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open youtube' in command:
            webbrowser.open("www.youtube.com")
            talk("opening youtube")    

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        talk("opening google")
            
    elif 'good bye' in command or 'stop' in command:
        talk("good bye")
        exit()

    else:
        temp = command.replace(' ','+')
        g_url="https://www.google.com/search?q="    
        res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
        print(res_g)
        talk(res_g)
        webbrowser.open(g_url+temp)

while True:
    run_alexa()