# 🎙️ Python Voice Assistant (Alexa-Like)

This is a voice-controlled assistant built with Python. It listens to your voice, recognizes commands using Google Speech Recognition, responds using text-to-speech, and performs basic tasks like opening websites, telling the time/date, or playing songs on YouTube.

## ✨ Features

- 🎤 **Voice Recognition**  
  Uses the microphone to listen and recognize speech in real time.

- 🗣 **Text-to-Speech Feedback**  
  Responds with spoken output using `pyttsx3`.

- 🔗 **Smart Commands**  
  Recognizes and acts on voice commands to:
  - 🔍 Open websites (YouTube, DuckDuckGo, ChatGPT, WhatsApp Web)
  - 🎵 Play YouTube videos by saying “play [song name]”
  - ⏰ Tell current time and date
  - 🛑 Exit gracefully by saying "exit", "stop", or "quit"

- 🧠 **Basic Error Handling**  
  Gracefully handles timeouts, recognition errors, and microphone silence.

---

## 🛠 Requirements

- Python 3.8 or higher  
- Microphone (for voice input)

Install dependencies:

```bash
pip install -r requirements.txt
