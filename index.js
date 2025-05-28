
const sendButton = document.getElementById('sendButton');
const textInput = document.getElementById('textInput');
const responseDiv = document.getElementById('response');
const voiceButton = document.getElementById('voiceButton');

sendButton.addEventListener('click', async () => {
  const text = textInput.value;
  const res = await fetch('http://127.0.0.1:5000/process_text', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  const data = await res.json();
  responseDiv.textContent = data.response;
  textInput.value = '';
});


voiceButton.addEventListener('click', () => {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    alert('Speech Recognition not supported in this browser.');
    return;
  }
  const recognition = new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.start();

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    textInput.value = transcript;
  };
});
