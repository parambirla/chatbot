async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput) return;

    // Display user's message
    const chatBox = document.getElementById("chatBox");
    const userMessage = document.createElement("div");
    userMessage.textContent = `You: ${userInput}`;
    chatBox.appendChild(userMessage);

    // Clear input field
    document.getElementById("userInput").value = "";

    // Send message to the backend
    try {
        const response = await fetch('https://chatbot-2r72.onrender.com/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: userInput })
        });
        const data = await response.json();

        // Display bot's response
        const botMessage = document.createElement("div");
        botMessage.textContent = `Bot: ${data.response || data.error}`;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to latest message

    } catch (error) {
        console.error('Error:', error);
    }
}
