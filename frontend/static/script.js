const chatMessages = document.getElementById("chat-messages");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

// Function to append a message to the chat
function appendMessage(content, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.textContent = content;
  chatMessages.appendChild(messageDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to the bottom
}

// Handle sending a message
sendButton.addEventListener("click", async () => {
  const userMessage = messageInput.value.trim();
  if (!userMessage) return;

  // Append user message to chat
  appendMessage(userMessage, "user");
  messageInput.value = "";

  // Send message to the server
  try {
    const response = await fetch("/response", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();
    const botResponse = data.response;

    // Append bot response to chat
    appendMessage(botResponse, "bot");
  } catch (error) {
    console.error("Error:", error);
    appendMessage("Error: Unable to connect to the server.", "bot");
  }
});

// Allow pressing Enter to send a message
messageInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    sendButton.click();
  }
});