import speech_recognition as sr
import pyttsx3
import time
import environment_variables
from dialogue_test import chat_assistant

def text_to_speech(text):
    tts_engine = pyttsx3.init()
    rate = 100 
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[1].id) 
    tts_engine.setProperty('rate', rate+50)
    tts_engine.say(text)
    tts_engine.runAndWait()
    
    
def start_recognizer():
    r = sr.Recognizer()
    source = sr.Microphone()
    print("System: Waiting for a keyword") 
    r.listen_in_background(source, callback) 
    time.sleep(1000000)

def callback(recognizer, audio):
    keywords = [("vega", 1), ("Vega", 1), ] 
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        if "vega" or "Vega" in  speech_as_text: 
            text_to_speech("Yes sir?") 
            print("Vega: Yes sir?")
            environment_variables.variable = True
            main_chat(environment_variables.variable)
    except sr.UnknownValueError: 
        print("Oops! Didn't catch that")        

def listen_for_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("System: Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio).strip()
        print(f"User: {user_input}")
        return user_input
    except sr.UnknownValueError:
        return "System: Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Error: {str(e)}"

def main_chat(variable):
    variable = environment_variables.variable
    while True:  
        if variable != True:
            start_recognizer()
        else:
            chat = listen_for_voice()
            chat_assistant(chat) 
            if environment_variables.variable == False:
                print("System: Waiting for a keyword") 
                break

