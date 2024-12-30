def convert_day(n):
    years=n//365
    remaining_days=n%365
    months=remaining_days//30
    remaining_days=remaining_days%30
    weeks=remaining_days//7
    days=remaining_days%7
    return years,months,weeks,days
n=int(input("enter number of days: "))
years,months,weeks,days=convert_day(n)
print(f"{years}years, {months}months, {weeks}weeks, {days}days")