"""Q.9
Subject Marks
Write a Python program to take subject names and marks for three subjects and store them in a dictionary
Display all subjects and marks and calculate the average marks."""



subjectmarks = {}

sum = 0
count = 0

for i in range(3):
	subject = input("Enter subject name = ")
	marks = input("Enter subject marks = ")

#print("subject marks =")

for subject in marks:
    print("Subject = ", subject)
    print("Marks = ", marks)

    sum = sum + marks
    count = count + 1

    average = sum / count

print("Total Marks = ", sum)
print("Average Marks = ", average)

 