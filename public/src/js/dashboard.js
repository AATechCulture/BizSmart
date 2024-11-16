document.getElementById("sendBtn").addEventListener("click", async function () {
  //   const userInput = document.getElementById("userInput").value;
  //   if (!userInput) {
  //     alert("Please enter a question or prompt.");
  //     return;
  //   }
  const userInput = "What is the formula for the area of a circle?";

  // Clear previous response
  document.getElementById("chatGPTResponse").innerHTML = "Loading...";

  const response = await fetch("https://api.openai.com/v1/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${openAiApiKey}`,
    },
    body: JSON.stringify({
      model: "gpt-4", // You can change this to other models like "gpt-3.5-turbo"
      prompt: userInput,
      max_tokens: 100, // Set the maximum response length
      temperature: 0.7, // Controls the randomness of the output
    }),
  });

  const data = await response.json();

  // Check if the API call is successful
  if (response.ok) {
    // Display GPT response
    const gptResponse = data.choices[0].text.trim();
    document.getElementById(
      "chatGPTResponse"
    ).innerHTML = `<b>ChatGPT says:</b> <br>${gptResponse}`;
  } else {
    document.getElementById(
      "chatGPTResponse"
    ).innerHTML = `<b>Error:</b> ${data.error.message}`;
  }
});
