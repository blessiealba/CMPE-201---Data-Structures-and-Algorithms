# Exercise 3: Diamond Shape (advance topic):
# Write a Python function named print_diamond that takes an odd integer n as an argument
# and prints a diamond shape with a width of n using the * character.
# For n = 5, the output should be:
#    *
#   ***
#  *****
#   ***
#    *
# Note: If an even number is passed, the function should return "Please provide an odd integer."

def print_dia(n):
    if n % 2 == 0:
        return "Invalid input! Please provide an odd number."
    
    #To create the upper part
    for i in range(n // 2 + 1):  
        spaces = (n // 2) - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)  
    
   #To create the lower part
    for i in range(n // 2 - 1, -1, -1):
        spaces = (n // 2) - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars) 

while True: 
    try: 
        n = int(input("Please enter a number: "))
        if n % 2 == 1:
            print_dia(n)
            break
        else: 
            print("Invalid input! Please provide an odd number.")
    except ValueError:
        print("Invalid input! Please provide an odd number.")