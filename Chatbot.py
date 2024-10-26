import openai

openai.api_key = "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"

def chatbot():
    print("Welcome to the GPT-3 Chatbot!")
    print("Type 'exit' to close the chatbot.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        elif user_input.lower() == "how is your mood today?":
            print("Chatbot: My mood is great, thank you for asking!")
            continue

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input + " ",
            max_tokens=2048,
            temperature=0.5
        )

        print("Chatbot:", response["choices"][0]["text"])

if __name__ == "__main__":
    chatbot()
