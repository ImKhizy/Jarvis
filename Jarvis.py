import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import re
import urllib.request
import urllib.parse
import time
import random
import tempfile
import subprocess

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


def speak(audio):
    subprocess.call("espeak -v espeak -v en-gb '{0}' -s 170 -p 30 -a 40 -g 4".format(audio), shell=True)

def setupfunc():
    global r
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 2)


def wishMe():
    speak('At your service sir')

def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print('Sorry sir I was unable to understand,')
        return "None"

    return query

def checkwhichrun(command):
    if "photoshop" in command:
        os.system('krita')
        speak('bringing up photo editing software on screen')
    # elif "code" in command:
    #     os.system('code')
    #     speak('Opening V S Code Now')
    elif "firefox" in command:
        os.system('firefox')
        speak('Showing Mozilla Firefox on monitor')
    elif "word" in command:
        os.system('libreoffice --writer')
        speak('Launching Word')
    elif "powerpoint" in command:
        os.system('libreoffice --impress')
        speak('Launching Powerpoint')
    elif "excel" in command:
        os.system('libreoffice --calc')
        speak('Launching Spreadsheet tool')
    else:
        command = command.lower()
        command = command.replace(" ", "")
        try:
            with tempfile.TemporaryFile() as tempf:
                proc = subprocess.Popen([command])
                proc.wait()
                tempf.seek(0)
        except Exception as e:
            if "No such file" in str(e):
                print("Requested program not found")
            else:
                proc = subprocess.Popen([command])
                proc.wait()
                
        


def queryfix(query, EnableQueryFilter):
    if "jarvis" in query:
        query = query.replace('jarvis ', '')
        if "hey" in query:
            query = query.replace('hey ', '')
            return query
        elif "hi" in query:
            query = query.replace('hi ', '')
            return query
        else:
            return query
    else:
        if EnableQueryFilter == True:
            return False
        else:
            return query

def praise():
    print("""Khizar, the designer of Jarvis, the currently running app, is a Genius Software Engineer born in March
            Second of Two thousand and Five. He was born in the city of Lahore, Punjab Pakistan. He wrote Jarvis at the age of 15 on an AMD A4 3400
            APU. """)
    speak("""Kheezrr, the designer of Jarvis, the currently running app, is a Genius Software Engineer born in March
        Second of Two thousand and Five. He was born in the city of Lahore, Punjab Pakistan. He wrote Jarvis at the age of 15 on an AMD A4 3400
         APU. """)


def logicalact(query):
        searchword = ["google", "search for", "tell me", "I wonder"]
        for item in searchword:
            if item in query:
                query = query.replace(item, "")
                webbrowser.open_new("https://www.google.com/search?q=" + query)
                speak('Googling ' + query)
        if 'play' in query or 'youtube' in query:
             tempolist = query.split()
             try:
                pind = tempolist.index("play")
             except:
                pind = tempolist.index("youtube")
            
             b = tempolist[pind:]
             query_string = urllib.parse.urlencode({"search_query=" : b})
             html_content = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
             print(html_content)
             search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
             webbrowser.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
             speak('Playing ' + b)

        elif "recipe for" in query:
            tempolist = query.split()
            commandpos = tempolist.index('for')
            s = " "
            b = s.join(tempolist[commandpos:])
            webbrowser.open_new("https://www.youtube.com/results?search_query=" + b)
            speak("Showing results for " + b )

        elif 'how' in query:
            tempolist = query.split()
            if "repair" in query or "fix" in query:
                s = " "
                webbrowser.open_new("https://stackoverflow.com/search?q=" + s.join(tempolist[3:]))
                speak("Showing results for " + query)

            elif 'cook' in query:
                s = " "
                query_string = urllib.parse.urlencode({"search_query" : s.join(tempolist[1:])})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                webbrowser.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
                speak("Showing results for " + query)
            elif 'are you' in query:
                speak('I am fine Sir. I appreciate you asking.')
            elif  'have you' in query:
                speak('I have been inactive for the most part.')
            elif  'were you' in query:
                speak('I was sleeping mostly.')
            else:
                s = " "
                webbrowser.open_new("https://www.google.com/search?q=" + (s.join(tempolist[1:])))
                speak("Showing results for " + query)

        elif 'what is the time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
                speak(f"Sir, the time is {strTime}")

        elif 'look up' in query or 'who is'in query or 'wikipedia' in query or 'identify' in query or 'who made you' in query:
            querylist = query.split(" ")
            if 'your designer' in query or 'your creator' in query:
                praise()

            elif querylist[-1] == "is":
                speak("Sir you didn't specify who to search for")

            else:
                speak('Searching Wikipedia... ')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia ")
                print("According to Wikipedia ")
                print(results)
                speak(results)

        elif 'run' in query or 'launch' in query:
            checkwhichrun(query)
        elif 'you' in query or 'yourself' in query or "jarvis" in query:
            if 'doing' in query and 'were' in query:
                speak("I was sleeping in my cozy script Sir. ")
            elif 'about' in query:
                speak("""I am just a voice assistant designed by Muhammad Kheezer, named Jarvis, as in the
                      Jarvis from Iron Man movies, of the Marvel Cinematic Universe.
                       """)
        notefound(query)


########################################################################################################################################################################################


takenote = ['note down' , 'write down', 'remember', 'take note', 'jot down', 'always keep in mind', ]
shownote = ['show notes', 'show my notes', 'show me my notes', 'show me all of my notes', 'show all of my notes']
readnote = ['read my notes', 'read all notes', 'read notes', 'read my observations', 'read all observations', 'read observations', 'quote me','read all of my quotes', 'read all of my observations', 'read all of my notes' ]
delnote =['clear all notes', 'delete all notes', 'erase all notes','clear my notes', 'delete my notes', 'erase my notes','clear notes', 'delete notes', 'erase notes', 'clear all of my notes', 'delete all of my notes', 'erase all of my notes']
def notefound(query):
    try:
        for item in takenote:
             if item in query:
                 query = query.split()
                 thatpos = (query.index("that") + 1)
                 note = ' '
                 note = note.join(query[thatpos:])
                 f = open("Notes.txt", "a+")
                 now = datetime.datetime.now()
                 year = '{:02d}'.format(now.year)
                 month = '{:02d}'.format(now.month)
                 day = '{:02d}'.format(now.day)
                 day_month_year = '{}-{}-{}'.format(year, month, day)
                 data = day_month_year + "  "+ note + "\r\n"
                 f.write(data)
                 f.close()
                 speak("Duly noted Sir")
                 print("NOTED")
        for item in shownote:
            if item in query:
                speak("Opening Notes")
                os.open("Notes.txt")
                print("Opening Notes")
        for item in readnote:
            if item in query:
                f = open("Notes.txt", "r")
                content = f.read()
                speak("Reading Your Notes")
                speak(content)
                f.close()
                print("READ NOTES")
        for item in delnote:
            if item in query:
                os.remove("Notes.txt")
                f = open("Notes.txt", "w+" )
                f.close()
                print("NOTES CLEARED")
                speak("Deleted All Notes Successfully.")
    except Exception as error:
            print("Sorry Sir, I am unable to perform this action at the momment.\n       " , error)
            speak("Sorry Sir, I am unable to perform this action at the momment")
            speak(str(error))



################################################################################
################################################################################
################################################################################
greets = ['Welcome back Sir, Jarvis at your Service', 'Welcome back Sir, How can I assist You today', 'Greetings Boss, Jarvis At Your Disposal', 'Greetings, Jarvis here. How may I help you']


speak(random.choice(greets))
print("Adjusting for Ambient Noise")
setupfunc()
print("Completed Adjusting")
speak("Ambient Noise Adjustment Complete")

def MainFunc1():
    EnableQueryFilter = True
    query = takeCommand().lower()
    query = queryfix(query, EnableQueryFilter)
    print(query)
    if query != False:
        if 'also' in query:
            query = query.split('also')
            logicalact(str(query[0]))
            logicalact(str(query[1]))
            logicalact(str(query[2]))
            MainFunc2()
        else:
            logicalact(query)
            MainFunc2()
    else:
        MainFunc1()
def MainFunc2():
    EnableQueryFix = False
    query = takeCommand().lower()
    query = queryfix(query, EnableQueryFix)
    print(query)
    if query != False:
        if 'also' in query:
            query = query.split('also')
            logicalact(str(query[0]))
            logicalact(str(query[1]))
            logicalact(str(query[2]))
            MainFunc2()
        else:
            logicalact(query)
            MainFunc2()
MainFunc1()
