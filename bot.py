import sys


def chatbot_response(user_input):
    # Chatbot response logic remains the same as before
    responses = {
        "hello": "Hello! How can I assist you?",
        "what's your name?": "I am Assistant GPT-3.5.",
        "how are you?": "I'm just a program, so I don't have feelings, but thank you for asking!",
        "what is Backend?": "Backend refers to the server-side of a web application or software that runs on the server and handles tasks such as data storage, processing, and interaction with the database. It is the part of the application that the users don't directly interact with but is essential for the proper functioning of the frontend.",
        "what tasks does the backend do?": "Common tasks that the backend handles include: Data storage and retrieval, Business logic, API handling, Integration, Security, and User management",
        "exit": "Thank you for talking to me. Goodbye!"
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand your question.")


def colored_print(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"


def main():
    assistant_name = colored_print("Assistant GPT-3.5", "green")
    print(f"{assistant_name}: Hello! I am a simple chatbot. Type 'exit' to quit.")

    while True:
        user_input = input(colored_print("You: ", "blue"))
        if user_input.lower() == 'exit':
            print(colored_print(f"{assistant_name}: Goodbye!", "green"))
            break
        else:
            response = chatbot_response(user_input)
            print(colored_print(f"{assistant_name}:", "green"), response)


if __name__ == "__main__":
    main()
