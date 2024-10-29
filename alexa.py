import speech_recognition as spre
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import time

alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[0].id)

# Recognizer initializatio
recognizer = spre.Recognizer()

def speak(text):
    alexa.say(text)
    alexa.runAndWait()

def listen_for_command():
    with spre.Microphone() as source:
        print("\nRemoving background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    
    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
        speak(f"You said: {command}")
        return command
    except spre.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except spre.RequestError as e:
        speak(f"Error with Google Speech Recognition service: {e}")
        return None

def execute_command(command):
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif 'open duckduckgo' in command:
        speak("Opening DuckDuckGo")
        webbrowser.open("https://www.duckduckgo.com")
    
    elif 'open chatgpt' in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    
    elif 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")
    
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        speak(f"Today's date is {current_date}")
    
    elif 'open whatsapp' in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    
    else:
        speak("I did not understand the command. Please try again.")

while True:
    print("Waiting for command...")
    command = listen_for_command()
    if command:
        execute_command(command)
    time.sleep(1) 