
const sendButton = document.getElementById('sendButton');
const textInput = document.getElementById('textInput');
const responseDiv = document.getElementById('response');

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
