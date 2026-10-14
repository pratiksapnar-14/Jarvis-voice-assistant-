import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import  requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "139219a924b74045b1147149b06b9916"

def speak_1(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
     
    

    # Initialize the mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the song
    pygame.mixer.music.play()

    # Keep the program running until the song finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")  



def aiprocess(command):
    client = OpenAI(api_key="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",)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. give short responses please"
        },
        {
            "role": "user",
            "content":command 
        }
    ]
)

    return completion.choices[0].message.content


def processCommand (c):
    if "open google" in c.lower():    
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:

         #JSON response 
            data = r.json()
            #extract the article
            articles = data.get('articles',[])
            #speak the headlines 
            for article in articles:
                speak(article['title'])

    else:
        #using openAI            
        output = aiprocess(c)
        speak(output)

if __name__=="__main__":
    speak("initializing Jarvis.....")
    while True:
        #wake command for "jarvis"
            # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        # recognize speech using google 
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen for command 
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

    
        except Exception as e:
            print("Error; {0}".format(e))