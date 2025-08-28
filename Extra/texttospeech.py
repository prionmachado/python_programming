import cowsay
import pyttsx3

engine = pyttsx3.init()

voice = input("What you want me to say? ")

if voice.strip(): 
    print(cowsay.cow(voice))  
    engine.setProperty('volume', 5.0)  
    engine.setProperty('rate', 150)  

    engine.say(voice)
    engine.runAndWait()
else:
    print("No input provided.")
