# Calculator using Python
print("Welcome to my calculator!\n", end = ""
      "Give me some numbers!\n")
# asks user for numbers and stores them
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#asks users to choose an operator
print("What would you like to do?")
op = input("Enter an operator (+ - * /): ")

if op == "+":
    print(f"{num1} + {num2} is equal to {round(num1 + num2, 1)}")
elif op == "-":
    print(f"{num1} - {num2} is equal to {round(num1 - num2, 1)}")
elif op == "*":
    print(f"{num1} x {num2} is equal to {round(num1 * num2, 1)}")
elif op == "/":
    print(f"{num1} divided by {num2} is {round(num1 / num2, 1)}")
