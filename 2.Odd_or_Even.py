"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""


user_input = int(input("Please enter a number > "))
nature = "even" if user_input % 2 == 0 else "odd"

print("The number you entered is {}.".format(nature))

#Extras

if user_input % 4 == 0:
    print("It is also a multiple of 4!")

num_to_check = int(input("Please enter the number to check > "))
num_to_divide_by = int(input("Please enter the divider > "))

divisible = "does" if num_to_check % num_to_divide_by == 0 else "does not"
print("{} {} divide evenly by {}".format(num_to_check,divisible, num_to_divide_by))

