def minutes_per_year(days_per_year, hours_per_day, minutes_per_hours):
    return days_per_year * hours_per_day * minutes_per_hours


print(minutes_per_year(365, 24, 60))
