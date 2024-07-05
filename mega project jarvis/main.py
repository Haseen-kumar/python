import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI 
from gtts import gTTS
import pygame
import os

 #pip install pocketsphinx


recognizer =sr.Recognizer()
engine=pyttsx3.init()
newsapi="e6fb1f74c8a54645979597e5728f213a"



def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):

     tts = gTTS(text)
     tts = gTTS(text='Hello', lang='en', slow=False)  # Normal speech
     tts.save('temp.mp3')
   

     pygame.init()

# Load the MP3 file
     pygame.mixer.music.load('temp.mp3')

# Play the MP3 file
     pygame.mixer.music.play()

# Wait for the music to finish playing
     while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)

# Stop the music
     pygame.mixer.music.unload()
     os.remove("temp.mp3")

# pygame.quit()
 



def aiprocess(command):
    client=OpenAI(api_key="sk-proj-EZ41WkBgPJ2l7Ief88l8T3BlbkFJ1X6EAHPT1bD6TLNMR7Yc",)



    completion = client.chat.completions.create(
     model="gpt-3.5-turbo",
     messages=[
     {"role": "system", "content": "You are a virtaul assistant name jarvis, skilled in explaining the task like alexa and google.give short responces please"},
     {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message




def processcommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://www.google.co.in/")

   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")

   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")

   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif c.lower().startswith("play"):
      song= c.lower().split(" ")[1]
      link= musiclibrary.music[song]
      webbrowser.open(link)

   elif "news" in c.lower():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
    r = requests.get(url)
 
    if r.status_code == 200:
        data = r.json()
        articles = data.get('articles', [])
      
        speak("Here are the latest news articles:")
        for article in articles:
               speak(article['title'])

   else:
      #let open ai handle the situation
       output=aiprocess(c)
       speak(output)

              
               
            
     
   

if __name__=="__main__":
    speak("intializing  jarvis...")
    # listen for the wake word..
    # obtain audio from the microphone
    while True:
       r = sr.Recognizer()
      
       print("recognizion...  ")
       try:
         with sr.Microphone() as source:
           print("listing..")
           audio = r.listen(source,timeout=2,phrase_time_limit=2)
       
           word=r.recognize_google(audio)
           if(word.lower()=="jarvis"):
              speak("ya")
              #listen for command
           with sr.Microphone() as source:
                print("jarvis active....")
                audio = r.listen(source)
                command=r.recognize_google(audio)

                processcommand(command)

        
       
       except Exception as e:
           print("error; {0}".format(e))  

