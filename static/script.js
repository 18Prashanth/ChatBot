async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userMessage = input.value.trim();
  if (!userMessage) return;

  // Show user message
  chatBox.innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage }),
  });

  const data = await response.json();

  // Show bot response
  chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}
