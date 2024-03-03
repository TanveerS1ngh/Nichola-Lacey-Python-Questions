# Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together.Display the finished result.

fname = input('Please provide your First name: ').lower()
sname = input('Please provide your Surname: ').lower()

print('Ok So your name is',fname.title()+' '+sname.title())