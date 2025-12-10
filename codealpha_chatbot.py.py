import random
def get_response(user_input):
    
    if "hello"  in user_input.lower():
            print("Chatbot: Hi there! How can I assist you today?")
            
    elif "how are you" in user_input:
            print("Chatbot: I'm doing well,  thanks for asking!")
    elif "what is your name" in user_input:
            print("Chatbot: I'm Chatbot, your virtual assistant.")
    elif "help" in user_input:
            print("Chatbot: Sure! What do you need help with?")
    elif "joke" in user_input:
            print("Chatbot: Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif "bye"in user_input:
            print("Chatbot: Goodbye! Have a great day!")
    else: 
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")
def chat():
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Chatbot: Goodbye!")
                break
            response = get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
        chat()