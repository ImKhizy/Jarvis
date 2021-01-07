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
                 hour = '{:02d}'.format(now.hour)
                 minute = '{:02d}'.format(now.minute)
                 day_month_year = '{}-{}-{}'.format(year, month, day)
                 data = day_month_year + note + "\r\n"
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
                f = open("Notes.txt", "r")
                os.remove("Notes.txt")
                f = open("Notes.txt", "w+" )
                f.close()
                print("NOTES CLEARED")
                speak("Deleted All Notes Successfully.")
    except Exception as error:
            print("Sorry Sir, I am unable to perform this action at the momment.\n       " , error)
            speak("Sorry Sir, I am unable to perform this action at the momment")
            speak(str(error))
