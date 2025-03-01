'''
TEAM DETAILS:-
Name of Student - Student Id
Manjinder Singh - 110097177
Harbhajan Singh - 110100089
Karan Vishavjit - 110099867
Khyati Shah     - 110090234
'''
from datetime import timedelta,datetime

# Answer 1:-
my_timedelta = timedelta(days=365, hours=5, minutes=1, seconds=0)

# Printing the timedelta
print("Ans. 1: Printing Time Delta - ", my_timedelta)

# Answer 2:-
# Getting Today's Date and Time
current_datetime = datetime.now()

# Printing Today's Date and Time
print("Ans. 2: Current Date Time is - ", current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f"))

# Answer 3:-
# Calculate the date and time two years from now
datetime_after_2_years = current_datetime + timedelta(days=365*2)

# Print the result
print("Ans. 3: Printing DateTime after 2 years - ", datetime_after_2_years.strftime("%Y-%m-%d %H:%M:%S.%f"))

# Answer 4:-
import random

# Now, first generating a random values for weeks and days
rand_weeks = random.randint(0, 6)
rand_days = random.randint(0, 5)

# Create a timedelta with random values of above
my_time_delta2 = timedelta(weeks=rand_weeks, days=rand_days)

# Calculate the future date and time
futu_datetime = current_datetime + my_time_delta2

# Print the result
print(f"Ans. 4: In {rand_weeks} weeks and {rand_days} days, the Date and Time will be - ", futu_datetime.strftime("%Y-%m-%d %H:%M:%S.%f"))

# Answer 5:-

# Calculate the date three weeks ago
datetime_before_three_weeks = current_datetime - timedelta(weeks=3)

# Define a list of day names
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Format the result as a string
res_string = f"Ans. 5: Day and Date before 3 weeks - {days_list[datetime_before_three_weeks.weekday()]} {datetime_before_three_weeks.strftime('%B %d, %Y')}."

# Printing the result.
print(res_string)

# Answer 6:-

from datetime import datetime, timedelta

# Intializing the date for Christmas for this year (December 25th, 2023)
christmas_date_for_curr_year = datetime(current_datetime.year, 12, 25)

# Checking if Christmas is passed for this year or not. 
if current_datetime > christmas_date_for_curr_year:
    # In case Christmas is already passed for this year.
    christmas_day = datetime(current_datetime.year + 1, 12, 25)
else:
    # In case Christmas is yet to come during the year.
    christmas_day = christmas_date_for_curr_year

# Number of days until next christmas.
days_left_for_christmas = (christmas_day - current_datetime).days

# Print the result
print(f"Ans. 6: {days_left_for_christmas} days are still left until next Christmas.")
