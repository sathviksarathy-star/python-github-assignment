"""
Monthly Savings Estimator
This program asks the user how much money they saved today,
estimates total monthly savings, and shows progress toward a monthly goal.
"""

# --- Task 1: Welcome message ---
print("Welcome to the Monthly Savings Estimator!")

# --- Task 2: Ask for user input ---
daily_input = input("How much money did you save today? $")

# --- Task 3 + Task 5: Convert input, perform calculation, handle errors ---
MONTHLY_GOAL = 300  # Set a monthly savings goal

try:
    daily_savings = float(daily_input)
except ValueError:
    print("Invalid input. Please enter a number such as 5 or 12.50.")
    exit()

# Check for negative numbers
if daily_savings < 0:
    print("Savings cannot be negative. Please enter a valid number.")
    exit()

# Perform calculation
estimated_monthly = daily_savings * 30  # simple 30-day estimate
progress_percent = (estimated_monthly / MONTHLY_GOAL) * 100
