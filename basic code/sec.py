"""Question 17: Write a Java program to convert seconds into hours, minutes, and seconds.
Asked In Basic program
Input:
Seconds = 3665

Output:
Hours = 1
Minutes = 1
Seconds = 5

Explanation:
1 hour = 3600 seconds.
3665 / 3600 gives 1 hour.
Remaining seconds are converted into minutes and seconds using division and modulus operations."""


Seconds = 3665

hours=3665/3600;
reminingsec=3665%3600
minutes=reminingsec/60
seconds=reminingsec%60
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)