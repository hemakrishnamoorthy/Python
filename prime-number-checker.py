def prime_checker(number):
  prime_flag = 'Y'
  if (number == 0 or number == 1):
    print(f"{number} is not a prime number")
  else: 
    for i in range(2,number):
       if number%i == 0:
          prime_flag = "N"
          break
    if prime_flag == 'N':
       print("It's not a prime number.")
    elif prime_flag =='Y':
       print("It's a prime number.")      


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Enter a number to check if it is prime: ")) # Check this number
prime_checker(number=n)