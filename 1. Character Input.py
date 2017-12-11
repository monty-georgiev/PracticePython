""""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many
    copies of the previous message.
    (Hint: order of operations exists in Python)

    Print out that many copies of the previous message on separate lines.
    (Hint: the string "\n is the same as pressing the ENTER button)

"""

user_name = input("Please input your name > ")
user_age = int(input("Please tell us your age > "))
print_count = int(input("Please enter a print count > "))

print("Hey, {} do you know that you'll be 100 in {}? \n".format(user_name, (2017-user_age)+100) * print_count)
