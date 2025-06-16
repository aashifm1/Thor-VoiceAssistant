import speech_recognition as spre
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import time

# Initialize TTS engine
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')

# Optional: Choose female English voice if available
for voice in voices:
    if "english" in voice.name.lower() and "female" in voice.name.lower():
        alexa.setProperty('voice', voice.id)
        break
else:
    alexa.setProperty('voice', voices[0].id)

# Initialize recognizer
recognizer = spre.Recognizer()

def speak(text):
    print(f"[Alexa]: {text}")
    alexa.say(text)
    alexa.runAndWait()

def listen_for_command():
    with spre.Microphone() as source:
        print("\n[System] Removing background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("[System] Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            speak(f"You said: {command}")
            return command
        except spre.WaitTimeoutError:
            speak("No voice detected. Please try again.")
        except spre.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except spre.RequestError as e:
            speak(f"Error with Google Speech Recognition: {e}")
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
        song = command.replace('play', '').strip()
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

    elif 'exit' in command or 'stop' in command or 'quit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I did not understand the command. Please try again.")

def main():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        print("\n[System] Waiting for command...")
        command = listen_for_command()
        if command:
            execute_command(command)
        time.sleep(1)

if __name__ == "__main__":
    main()
    
