from datetime import datetime

def get_days_from_today(date: str):
    try:
        # Convert the string to a datetime object
        date_object = datetime.strptime(date, "%Y-%m-%d")
        # Get the current date
        date_now = datetime.today()
        # Calculate the difference
        difference = date_now - date_object   
        # Return the number of days
        return difference.days
    except ValueError as e:
        # Handle invalid date format
        print(f"Error: The entered date '{date}' does not match the format 'YYYY-ММ-DD'")
    except Exception as e:
        print(e)

# Отримання дати від користувача
date = input("Enter the date in the format 'YYYY-MM-DD' >>> ")
result = get_days_from_today(date)

if result is not None:
    print(f"The number of days from {date} to today is: {result}")
