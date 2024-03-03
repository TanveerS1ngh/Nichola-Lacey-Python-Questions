# Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”,otherwise display “Thank you”.

user = int(input("Enter any number under 20: "))

if user >= 20:
    print("Too high")
else:
    print("Thank you")