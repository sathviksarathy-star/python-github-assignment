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

# --- Task 4: Display the results clearly ---
print("\n Savings Summary")
print("-----------------------------")
print(f"Today's savings: ${daily_savings:.2f}")
print(f"Estimated monthly savings: ${estimated_monthly:.2f}")
print(f"Monthly goal: ${MONTHLY_GOAL:.2f}")
print(f"Progress toward goal: {progress_percent:.1f}%")

# Progress message
if progress_percent < 50:
    message = "You're off to a good start—keep saving!"
elif progress_percent < 100:
    message = "Great job! You're getting close to your monthly goal."
else:
    message = "Excellent! You're on track to meet or exceed your savings goal."

print(message)

# --- Task 6: Cleanup done, program complete ---