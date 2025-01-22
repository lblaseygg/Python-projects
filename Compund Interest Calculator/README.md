# Python Interest Calculator

This Python program calculates the total balance after applying compound interest to an initial principal amount. The program prompts the user to enter the principal amount, interest rate, and time in years to compute the final balance.

## Features

- **User Input:** Prompts the user to enter the principal amount, interest rate, and time (in years).
- **Validation:** Ensures all inputs are valid (positive numbers only).
- **Compound Interest Calculation:** Uses the compound interest formula to calculate the final balance after the specified period.
- **Result:** Displays the total balance after the interest has been applied.

## Formula for Compound Interest

The total balance is calculated using the following formula:
```
Total = P * (1 + r / 100) ^ t
```
Where:
- `P` is the principal amount
- `r` is the annual interest rate
- `t` is the time period in years

## Example
- Enter the principal amount: 1000 Enter the interest rate: 5 Enter the time in years: 3 Your balance after 3 year/s: $1157.63

## Requirements

- Python 3.x or later.

## How to Run

1. Clone the repository or download the Python file.
2. Open a terminal or command prompt.
3. Run the Python script using the command:

   ```bash
   python interest_calculator.py