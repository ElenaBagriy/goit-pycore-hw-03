import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []

    # Input validation
    if min <1 or max > 1000 or max < min or quantity > (max - min + 1) or quantity <= 0:
        print("You entered incorrect data.")
        return lottery_numbers
    
    # Generating unique random numbers
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        random_number = random.randint(min, max)
        unique_numbers.add(random_number)

    # Returning the sorted list
    lottery_numbers = sorted(list(unique_numbers))
    return lottery_numbers

# Getting input parameters from the user
try:
    min = int(input("Enter the minimum possible number in the range (at least 1) >>> "))
    max = int(input("Enter the maximum possible number in the range (no more than 1000) >>> "))
    quantity = int(input("Enter the number of numbers to select (between min and max) >>> "))

    # Calling the function and printing the result
    lottery_numbers = get_numbers_ticket(min, max, quantity)
    print("Your lottery numbers:", lottery_numbers)
except ValueError as e:
    # Handling the case when a non-numeric value is entered
    print("Error: The entered value is not a number")
except Exception as e:
    # Handling any other unexpected errors
    print(f"Unexpected error: {e}")