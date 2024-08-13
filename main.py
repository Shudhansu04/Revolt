import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
from openai import OpenAI
from gtts import gTTS
 
import os


recogniser=sr.Recognizer()
ttsx= pyttsx3.init()
newsapi="9b015c49927e42ba8e5d14c649f16e28"

def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()

def speak(text):
    tts= gTTS( text)
    tts.save("temp.mp3")
    # Initialize the mixer module
    pygame.mixer.init()

# Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play the MP3 file
    pygame.mixer.music.play()

# Keep the program running until the music stops
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def aiProcess(command):
    client = OpenAI(api_key="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")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a virtual  assistant, skilled in general tasks like alexa and google cloud. Give short responses please"},
    {"role": "user", "content": command}
    ]
     )

    return completion.choices[0].message.content

def processCommand(c):
    if( "open google " in c.lower()):
        webbrowser.open("https://www.google.com")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://facebook.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://youtube.com")
    elif("open linkedin" in c.lower()):
        webbrowser.open("https://linkedin.com")
    elif("open instagram" in c.lower()):
        webbrowser.open("https://instagram.com")  
    elif(c.lower().startswith("play")):
         song=c.lower().split(" ")[1]
         link=musicLibrary.music[song]
         webbrowser.open(link)
    elif("news" in c.lower()):
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=API_KEY= {newsapi}")
        if(r.status_code==200):
            #Parse the JSON reponse
            data=r.json()

            #Extract the articles
            articles=data.get("articles",[])

            #Print the headlines
            for article in articles:
                speak(article["title"])

    else:
        #Let handle open ai
         output=aiProcess(c)
         speak(output)



if __name__=="__main__":
    speak("Initializing Revolt.....")
    #listen for the wake word revolt
    while True:
        r= sr.Recognizer()
        
        
        print("recognizing....")

        # recognize speech using google cloud
        try:
            with sr.Microphone() as source:
               print("Listening.....")
               audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word= r.recognize_google(audio)
            if(word.lower()=="revolt"):
              speak("yes boss....")
              #listen for commands
              with sr.Microphone() as source:
                  print("Revolt Active.....")
                  audio=r.listen(source)
                  command= r.recognize_google(audio)



                  processCommand(command)

         
        except Exception as e:
            print(e)



