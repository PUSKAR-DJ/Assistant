# Personal Assistant (Voice & AI Powered)

A simple personal assistant web app that accepts text or voice commands, opens apps, performs web searches, and answers questions using Google Gemini AI.

---

## Features

- **Text & Voice Input:** Type or speak your commands in the browser.
- **Open Applications:** Opens Windows apps by name.
- **Web Search:** Searches Google for your query.
- **AI Assistant:** Answers general questions using Gemini AI.
- **Text-to-Speech:** Speaks responses aloud on your computer.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd Assistant
```

### 2. Install Python Dependencies

```sh
pip install -r requirements.txt
```

### 3. Set Up Your Gemini API Key

- Create a `.env` file in the project root (already included in this repo):
  ```
  GEMINI_API_KEY=your_actual_gemini_api_key_here
  ```
- **Never share your API key publicly!**

### 4. Run the Backend

```sh
python backend.py
```

The Flask server will start at `http://127.0.0.1:5000`.

### 5. Open the Frontend

- Open `index.html` in your web browser (preferably Chrome or Edge for voice support).

---

## Usage

1. **Type** your command or **click the 🎤 Speak button** and say your command.
2. Click **Send**.
3. The assistant will:
   - Open apps if you say `open <appname>`
   - Search Google if you say `search <query>`
   - Answer questions using Gemini AI otherwise
   - Speak the response aloud

---

## Example Commands

- `open notepad`
- `search weather in London`
- `What is the capital of France?`

---

## Requirements

- Python 3.8+
- Windows OS (for app opening feature)
- Chrome/Edge browser (for voice input)

---

## Security

- Your Gemini API key is stored in `.env` (which is gitignored).
- **Do not share your `.env` file.**

---

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [pyttsx3](https://pyttsx3.readthedocs.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyautogui](https://pyautogui.readthedocs.io/)

---

## License

MIT License
