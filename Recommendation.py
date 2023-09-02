def get_recommendations(category):
    recommendations = {
        "movies": [
            "Yeh Jawani Hai Dewani",
            "Five Feet Apart",
            "Harry Potter",
            "Twilight",
            "Dear Zindagi",
            "The Fault in our stars",
        ],
        "fashion brands": [
            "ALDO",
            "Bershika",
            "BIBA",
            "Channel",
            "DIOR",
        ],
        "restaurant": [
            "Bhojohori Manna",
            "Crystal Chopstick",
            "Suchali's artisan bakehouse",
            "The manifest restro",
            "La artisan bistro",
        ]
    }
    
    return recommendations.get(category.lower(), [])

def ai_recommendation_chatbot():
    print("AI Recommendation Chatbot: Hello! I'm your AI recommendation chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI Recommendation Chatbot: Bye!")
            break
        
        recommendations = get_recommendations(user_input)
        
        if recommendations:
            print("AI Recommendation Chatbot: Here are some recommendations for you:")
            for idx, recommendation in enumerate(recommendations, start=1):
                print(f"{idx}. {recommendation}")
        else:
            print("AI Recommendation Chatbot: I'm sorry, but I couldn't find any recommendations.")

ai_recommendation_chatbot()