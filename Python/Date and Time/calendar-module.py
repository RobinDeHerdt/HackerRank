# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

# Format: "MM DD YYYY"
input_date = input()

# Make sure all input values are converted to int
month, day, year = map(int, input_date.split())

# Create a list of day names - monday will be at index 0!
week_name_list = list(calendar.day_name)

# Calculate day number for the given date. By default 0 = monday.
day_number = calendar.weekday(year, month, day)

day_name = week_name_list[day_number]
print(day_name.upper())
