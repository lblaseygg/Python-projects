# Python Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Enter a valid amount")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Enter a valid interest rate")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Enter valid years")
    else:
        break

# formula for calculating compound interest
total = principle * pow((1 + rate / 100), time)
print(f"Your balance after {time} year/s: ${total:.2f}")