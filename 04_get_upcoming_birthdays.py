from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Get today's date
    today = datetime.today().date()
    # Calculate the date one week ahead
    delta_date = today + timedelta(days=7)
    # Initialize the list for storing upcoming birthdays
    congratulations_list = []
    
    for user in users:
        # Get the birthday string from the user data
        birtday_string = user.get("birthday")
        # Convert the birthday string to a date object
        birthday = datetime.strptime(birtday_string, "%Y.%m.%d").date()
        # Update the birthday year to the current year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If the birthday has already passed this year, move it to the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if the birthday falls within the next 7 days
        if today <= birthday_this_year <= delta_date:
            congratulation_date = birthday_this_year
            # If the birthday falls on a Saturday, move it to the following Monday
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            # If the birthday falls on a Sunday, move it to the following Monday
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)
            
            # Add the user's name and congratulation date to the list
            congratulations_list.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    # Return the list of upcoming birthdays
    return congratulations_list

# Test example
users = [
    {"name": "John Doe", "birthday": "1985.01.03"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Congratulations list this week:", upcoming_birthdays)