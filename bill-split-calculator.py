#this is the Bill split calculator which will ask for the total bill amount, the number of people in the group and percentage of tip.
print("Welcome to the bill split calculator")
#Enter the total bill amount
bill_amt = float(input("Enter the total bill amount: $"))
#Enter the tip percentage: Enter 10, 12 or 15%
tip = int(input("Enter the tip percentage: 10, 12 or 15%: "))
#calculate the tip amount
tip_amt = bill_amt * tip / 100
#calculate the total amount including tip
total_amt = bill_amt + tip_amt
#Enter the number of people in the group
count = int(input("Enter the number of people in the group: "))
# Calculate the share of each person
share = "{:.2f}".format(total_amt / count)
#print the share amount
print(f"Each person should pay ${share}")
