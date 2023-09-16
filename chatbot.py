def botresponse(userInput):
    userInput = userInput.lower()
    
    if "hello" in userInput:
        return "Hi there!"
    elif "how are you" in userInput:
        return "I'm good, how is your health."
    elif "i'm good" in userInput:
        return "That's great!"
    elif "who created you?" in userInput:
        return "I'm an AI, created by coding."
    elif "can we have a chitchat together?" in userInput:
        return "Definently, I am your alltime companion."
    elif "do you play outside?" in userInput:
        return "No, I am an AI, How Can I."
    elif "alright then we would chat again later" in userInput:
        return "Already? Goodbye!"
    else:
        return "Sorry friend, I don't know that yet."


print("Chatbot: Hi! I'm your simple chatbot. Type 'hello' to start chatting, and 'bye' to exit.")
while True:
    userInput = input("You: ")
    if userInput.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = botresponse(userInput)
    print("Chatbot:",response)