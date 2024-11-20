from groq import Groq

# Initialize the Groq client
client = Groq()

def ai_chatbot():
    print("AI Chatbot: Hi there! I am your AI assistant. Type 'exit' to end the chat.")
    
    # Loop to continuously interact with the user
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("AI Chatbot: Goodbye!")
            break
        
        # Send the user's message to the AI model
        try:
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": user_input}],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )
            
            # Stream and display the AI's response
            print("AI Chatbot: ", end="")
            for chunk in completion:
                print(chunk.choices[0].delta.content or "", end="")
            print()  # Move to the next line after response

        except Exception as e:
            print(f"Error: {e}")
            break

# Run the chatbot
if __name__ == "__main__":
    ai_chatbot()

