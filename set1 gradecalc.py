Average and Grade Calculation

m1, m2, m3 = map(int, input("Enter marks of 3 subjects: ").split())

average = (m1 + m2 + m3) / 3

if 90 <= average <= 100:
    grade = "O"
elif 80 <= average <= 89:
    grade = "A+"
elif 70 <= average <= 79:
    grade = "A"
elif 60 <= average <= 69:
    grade = "B+"
elif 50 <= average <= 59:
    grade = "B"
elif 45 <= average <= 49:
    grade = "C"
elif 40 <= average <= 44:
    grade = "P"
else:
    grade = "F"

print("Average is:", round(average, 2))
print("Grade is:", grade)

OUTPUT
Enter marks of 3 subjects: 98 76 56
Average is: 76.67
Grade is: A
