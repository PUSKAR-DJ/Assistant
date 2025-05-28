import speech_recognition as sr
import pyttsx3
from flask import Flask, request
import webbrowser
import pyautogui
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_app(app_name):
    # Use pyautogui to find and click on the app's icon
    pyautogui.press('win')  # Press the Windows key
    pyautogui.type(app_name)  # Type the app name
    pyautogui.press('enter')  # Press Enter

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.json['text']

    if 'open' in text:
        app_name = text.split('open ')[1]
        open_app(app_name)
        speak(f"Opening {app_name}.")
    elif 'search' in text:
        query = text.split('search ')[1]
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}.")
    else:
        speak("I couldn't understand that. Please try again.")

    return {'response': 'Task completed'}

if __name__ == '__main__':
    app.run()