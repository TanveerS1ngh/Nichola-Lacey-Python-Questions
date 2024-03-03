# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range,display the message “Thank you”, otherwise display the message “Incorrect answer”.

user = int(input("Please enter a number between 10 and 20: "))

if user >= 10 and user <= 20:
    print("Thank you")
else:
    print("Incorrect answer")