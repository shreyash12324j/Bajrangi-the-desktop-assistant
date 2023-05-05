import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
# this line is for get voices 
voices = engine.getProperty('voices')
# print(voices[1].id)
# this line for ste voices 1 refers to female voice and 0 refers to male voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # this function is used to get voice from Ai, bot speak the statement which is defined in main function
    engine.runAndWait()

# this function i create for introductory remarks by Bajrangi
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Bajrangi. Please tell me how may I assist you")       

# this function takes microphone input from the user and returns string output
def takeCommand():

    # recognizer is a class it helps to recognize the audio i.e., microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# this function is used to send email to any gmail first to her you have to provide id and password to whom you have to send 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Main function to define statement speak by Ai 
if __name__ == "__main__":
    # speak("My Name is Shreyash Tiwari")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open leetcode' in query:
            webbrowser.open("https://leetcode.com/problemset/algorithms/?page=1&search=Reverse+words+in+a+string")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open gpt' in query:
            webbrowser.open("https://chat.openai.com/auth/login")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")    

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "youremail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Shreyash. I am not able to send this email")