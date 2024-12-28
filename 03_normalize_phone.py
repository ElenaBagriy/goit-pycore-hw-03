import re

def normalize_phone(phone_number: str):
    # Remove all characters except digits
    pattern = r"\D"
    replacement = ""
    formatted_name = re.sub(pattern, replacement, phone_number)

    # Check if the number starts with 380 or 0
    # Replace it with +380 if necessary
    pattern2 = r"^380|^0"
    replacement2 = "+380"

    match = re.search(pattern2, formatted_name)
    if match:
        # If the number starts with 380 or 0, replace the start with "+380"
        formatted_name = re.sub(pattern2, replacement2, formatted_name) 
        return formatted_name
    else:
        # If the number does not start with 380 or 0, prepend "+380" manually
        formatted_name = f'+380{formatted_name}'
    # Return the normalized phone number
    return formatted_name
    

# List of raw phone numbers for testing
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "50 111 22 11   ",
]

# Apply the normalization function to all phone numbers
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Output the results
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

