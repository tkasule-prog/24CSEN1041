 Salary Calculation SET1 B

hours = int(input("Enter total hours worked: "))

if hours <= 8:
    grosssalary = hours * 200
else:
    grosssalary = (8 * 200) + ((hours - 8) * 300)

if grosssalary > 5000:
    tax = grosssalary * 0.05
else:
    tax = 0

netsalary = grosssalary - tax

print("Gross salary:", int(grosssalary))
print("Tax:", int(tax))
print("Net salary:", int(netsalary))
