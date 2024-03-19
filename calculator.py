logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
  return (n1 + n2)


def subtract(n1, n2):
  return (n1 - n2)


def multiply(n1, n2):
  return (n1 * n2)


def divide(n1, n2):
  return (n1 / n2)


def calculator():
  print(logo)
  result = 0
  shld_continue = True
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
  operators = list(operations.keys())
  num1 = float(input("Enter your first number: "))

  while shld_continue:
    oper = input(f"Pick your operator: {operators} ")
    num2 = float(input("Enter your second number: "))
    calc_method = operations[oper]
    result = calc_method(num1, num2)
    print(f"{num1} {oper} {num2} = {result}")
    if input(
        f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: "
    ).lower() == "y":
      num1 = result
    else:
      shld_continue = False
      calculator()


calculator()
