const { ipcRenderer } = require('electron');
const SpeechRecognition = require('web-speech-api').SpeechRecognition;

const sendButton = document.getElementById('sendButton');
const textInput = document.getElementById('textInput');

const recognition = new SpeechRecognition();
recognition.lang = 'en-US'; // Set the language

const microphoneButton = document.createElement('button');
microphoneButton.textContent = 'Speak';
document.body.appendChild(microphoneButton);

microphoneButton.addEventListener('click', () => {
  recognition.start();
});

recognition.onresult = (event) => {
  const transcript = event.results[event.results.length - 1][0].transcript;
  textInput.value = transcript;
  ipcRenderer.send('process_text', transcript);
};

sendButton.addEventListener('click', () => {
  const text = textInput.value;
  ipcRenderer.send('process_text', text);
  textInput.value = '';
});

ipcRenderer.on('response', (event, response) => {
  console.log(response);
});