import speech_recognition as sr
import pyttsx3
from flask import Flask, request
import webbrowser
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
import os

if os.environ.get('DISPLAY'):
    import pyautogui



load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY) 

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
        prompt = f"You are a helpful assistant. User said: '{text}'. Respond appropriately."
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(prompt)
            ai_reply = response.text.strip()
            speak(ai_reply)
            return {'response': ai_reply}
        except Exception as e:
            error_msg = "Sorry, I couldn't process your request."
            speak(error_msg)
            return {'response': error_msg}

    return {'response': 'Task completed'}

if __name__ == '__main__':
    app.run()