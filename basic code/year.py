"""Question 18: Write a Java program to convert days into years, months, and weeks.
Asked In Basic program
Input:
Days = 400

Output:
Years = 1
Months = 1
Weeks = 1

Explanation:
1 year = 365 days.
After subtracting 365 days, the remaining days are divided into months (30 days each) and weeks (7 days each)."""



Days=400

years=Days/365
remainingday=Days%365
months=remainingday/30
remainingday=remainingday%30
weeks=remainingday/7

print("Years=",years)
print("Months=",months)
print("Weeks=",weeks)