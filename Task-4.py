
def get_response(user_input: str) -> str:
    """Return a predefined reply based on keywords in the user's message."""

    # Normalize input: lowercase + strip extra spaces so matching is
    # not case-sensitive and ignores accidental whitespace.
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm a simple rule-based chatbot."

    elif "help" in text:
        return "You can say things like: hello, how are you, your name, bye."

    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def chat() -> None:
    """Run the chatbot loop: keep asking for input until the user says bye."""
    print("Chatbot: Hello! Type 'bye' anytime to end our chat.")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        # End the loop once the chatbot has said goodbye
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()