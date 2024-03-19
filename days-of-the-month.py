def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return(True)
      else:
        return(False)
    else:
      return(True)
  else:
    return(False)
  
def days_in_month(yr, mo):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if mo == 2:
     if is_leap(yr):
       return 29
     else:
       return 28
  elif mo -1 <= 11:
     return month_days[mo-1]
  
#🚨 Do NOT change any of the code below 
print("Welcome to the Days of a month program.\n")
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
days = days_in_month(year, month)
print(f" {month} {year} has {days}days. "))

