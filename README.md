# Homework Assignment goit-pycore-hw-03: Working with Date, Time, and Advanced String Manipulation

## Task 1: Calculate the number of days from a given date to today

### Function: `get_days_from_today(date)`

This function calculates the number of days between the given date and the current date.

#### Requirements:
1. The function takes one parameter: `date` — a string representing a date in the format 'YYYY-MM-DD' (e.g., '2020-10-09').
2. The function returns an integer indicating the number of days from the given date to today. If the given date is in the future, the result will be negative.
3. The function should ignore the time (hours, minutes, seconds) and only consider the days.
4. Use the Python `datetime` module to work with dates.

#### Implementation Steps:
1. Import the `datetime` module.
2. Convert the date string in the format 'YYYY-MM-DD' to a `datetime` object.
3. Get the current date using `datetime.today()`.
4. Calculate the difference between the current date and the given date.
5. Return the difference in days as an integer.

#### Example:

If today is May 5, 2021, calling `get_days_from_today("2021-10-09")` should return `-157`, since October 9, 2021, is 157 days later than May 5, 2021.

#### Evaluation Criteria:
1. Correctness: The function must accurately calculate the number of days between the two dates.
2. Exception Handling: The function should handle incorrect date formats.
3. Code Readability: The code should be clean and well-documented.

## Task 2: Generate a unique set of random lottery numbers

### Function: `get_numbers_ticket(min, max, quantity)`

This function generates a set of unique random numbers for a lottery ticket, based on a given range and quantity.

#### Requirements:
1. **Parameters**:
   - `min`: The minimum possible number in the set (greater than or equal to 1).
   - `max`: The maximum possible number in the set (less than or equal to 1000).
   - `quantity`: The number of unique numbers to be selected (must be between `min` and `max`).
2. The function generates the specified number of unique random numbers within the given range.
3. The function returns a list of randomly selected, sorted numbers. The numbers should not repeat.
4. If the parameters do not meet the specified constraints, the function returns an empty list.

#### Implementation Steps:
1. Check that the input parameters meet the constraints.
2. Use the `random` module to generate random numbers.
3. Ensure the uniqueness of the numbers using a set or other mechanism.
4. Return the sorted list of unique numbers.

#### Example:

Suppose you need to select 6 unique numbers for a lottery ticket, with numbers ranging from 1 to 49. You can use the function like this:

```python
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
```

This call will return a list of 6 random, unique, and sorted numbers, such as [4, 15, 23, 28, 37, 45]. Each time the function is called, a different set of numbers will be generated.

#### Evaluation Criteria:
1. Input Validation: The function must check the validity of the input parameters.
2. Uniqueness of Results: All numbers in the result must be unique.
3. Compliance with Requirements: The result must be a sorted list of unique numbers.
4. Code Readability: The code should be clean and well-documented.

## Task 3: Normalize phone numbers for SMS distribution

### Function: `normalize_phone(phone_number)`

This function normalizes phone numbers to a standard format, ensuring they are suitable for SMS distribution. The function will remove any unwanted characters and add the international country code if necessary.

#### Requirements:
1. **Parameter**:
   - `phone_number`: A string containing a phone number in any format (e.g., with spaces, parentheses, or dashes).

2. The function should:
   - Remove all non-numeric characters, except for the '+' symbol.
   - If the number does not include an international country code, add the country code `+38` (for Ukraine).
   - If the number already includes the country code `380`, replace it with `+38`.

3. **Return**:
   - The function should return the normalized phone number as a string in the format `+38XXXXXXXXX`.

#### Implementation Steps:
1. Use the `re` module to remove unwanted characters from the phone number.
2. Check if the phone number starts with the `+` symbol. If not, ensure it includes the `+38` country code where applicable.
3. Return the normalized phone number.

#### Example:

Given the following raw phone numbers:

```python
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
```
You can use the function like this:

```python
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS distribution:", sanitized_numbers)
```
Output:

```python
Normalized phone numbers for SMS distribution: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```
#### Evaluation Criteria:
1. Correctness: The function should correctly handle various phone number formats, adding the proper country code where needed.
2. Code Readability: The code should be clean, well-organized, and well-documented.
3. Use of Regular Expressions: The function should use regular expressions efficiently to clean the phone number.

## Task 4: Get upcoming birthdays within the next 7 days

### Function: `get_upcoming_birthdays(users)`

This function helps to determine which colleagues' birthdays fall within the next 7 days, including the current day. It also considers weekends and moves the congratulation date to the next Monday if necessary.

#### Requirements:
1. **Parameter**:
   - `users`: A list of dictionaries, where each dictionary contains:
     - `name`: A string with the user's name.
     - `birthday`: A string representing the user's birthday in the format 'YYYY.MM.DD'.
   
2. The function should:
   - Identify birthdays within the next 7 days, including today.
   - If a birthday falls on a weekend (Saturday or Sunday), the congratulation date should be moved to the following Monday.
   
3. **Return**:
   - A list of dictionaries with the `name` of the user and the `congratulation_date` in the format 'YYYY.MM.DD'.

#### Implementation Steps:
1. Convert each user's birthday from string to a `datetime` object.
2. Get the current date using `datetime.today().date()`.
3. Iterate through the `users` list and check if the birthday falls within the next 7 days.
4. If the birthday falls on a weekend, move the congratulation date to the next Monday.
5. Return a list of dictionaries with the `name` and `congratulation_date` for each user whose birthday falls within the specified range.

#### Example:

Given the following `users` list:

```python
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
```
You can use the function like this:

```python
upcoming_birthdays = get_upcoming_birthdays(users)
print("Upcoming birthdays this week:", upcoming_birthdays)
```
If today is 2024.01.22, the output will be:

```python
Upcoming birthdays this week: [
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]
```

#### Evaluation Criteria:
1. Correctness: The function must correctly determine the upcoming birthdays within the next 7 days.
2. Handling Weekends: If a birthday falls on a weekend, the function must move the congratulation date to the following Monday.
3. Code Readability: The code should be clean, well-organized, and well-documented.