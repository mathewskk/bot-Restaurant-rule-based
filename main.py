import random

def restaurant_chatbot():

    print("🍴 Welcome to Foodie Restaurant Chatbot!")
    print("Type 'bye' to exit.\n")

    desserts = ["Chocolate Cake", "Ice Cream Sundae", "Brownie", "Cheesecake"]
    drinks = ["Lemonade", "Fresh Juice", "Cold Coffee", "Milkshake"]
    combos = ["Pizza + Coke", "Burger + Fries + Drink", "Pasta + Garlic Bread"]
    specials = ["Chef Special Pizza", "Grilled Chicken Pasta", "Signature Burger"]

    while True:
        user = input("You: ").lower()

        # Greeting
        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you today?")

        # Menu
        elif "menu" in user:
            print("Bot: Our popular items are Pizza, Burger, Pasta, and Salad.")

        # Vegetarian suggestion
        elif "veg" in user or "vegetarian" in user:
            print("Bot: You can try Veg Pizza, Paneer Burger, or Fresh Salad.")

        # Spicy food
        elif "spicy" in user:
            print("Bot: Try our Spicy Chicken Pizza or Mexican Burger.")

        # Desserts
        elif "dessert" in user or "sweet" in user:
            print("Bot: Our desserts include:", ", ".join(desserts))

        # Drinks
        elif "drink" in user or "beverage" in user:
            print("Bot: We serve:", ", ".join(drinks))

        # Combos
        elif "combo" in user:
            print("Bot: Popular combos are:", ", ".join(combos))

        # Today's Special
        elif "special" in user:
            print("Bot: Today's special is:", random.choice(specials))

        # Opening hours
        elif "hours" in user or "open" in user:
            print("Bot: We are open from 10 AM to 10 PM every day.")

        # Location
        elif "location" in user or "where" in user:
            print("Bot: We are located at Main Street, City Center.")

        # Offers
        elif "offer" in user or "discount" in user:
            print("Bot: Current offer: Get 10% off on all combos!")

        # Food tips
        elif "tips" in user:
            print("Bot: Tip: Pair pasta with fresh juice or lemonade!")

        # Reservation
        elif "book" in user or "reservation" in user:
            print("Bot: You can call 9876543210 to reserve a table.")

        # Random dish suggestion
        elif "suggest" in user or "recommend" in user:
            all_items = desserts + drinks + combos + specials
            print("Bot: I recommend you try:", random.choice(all_items))

        # Ask user preference
        elif "preference" in user or "like" in user:
            pref = input("Bot: Do you prefer Veg or Non-Veg? ").lower()

            if "veg" in pref:
                print("Bot: You may like Veg Pizza or Paneer Pasta.")
            else:
                print("Bot: You may like Chicken Burger or Grilled Chicken Pasta.")

        # Mood based suggestion
        elif "mood" in user:
            mood = input("Bot: What is your mood? (happy / sad / tired / party) ").lower()

            if mood == "happy":
                print("Bot: Celebrate with Pizza and Milkshake!")
            elif mood == "sad":
                print("Bot: Ice Cream and Chocolate Cake will cheer you up!")
            elif mood == "tired":
                print("Bot: Try Pasta with Fresh Juice for energy.")
            elif mood == "party":
                print("Bot: Order Combos and Cold Coffee!")
            else:
                print("Bot: I suggest trying our Chef Special Pizza.")

        # Exit
        elif user == "bye":
            print("Bot: Thank you for visiting! Have a nice day 😊")
            break

        # Default response
        else:
            print("Bot: Sorry, I didn’t understand. Try asking about menu, desserts, drinks, combos, offers, or suggestions.")

restaurant_chatbot()
