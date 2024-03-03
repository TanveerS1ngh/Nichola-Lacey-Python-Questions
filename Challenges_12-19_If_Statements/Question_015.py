# Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.

user = input("Enter your favourite colour: ")

if user == "red" or user == "RED" or user == "Red":
    print("I like red too")
else:
    print("I don't like " + user + ", I prefer red")