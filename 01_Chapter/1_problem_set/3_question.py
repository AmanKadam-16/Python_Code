# Install and Use any external module / package
# pip install pttsx3 ~ a TTS python library
 
import pyttsx3
engine = pyttsx3.init()
engine.say("Wakeup humans, this is ultron!")
engine.runAndWait()