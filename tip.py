#Tip Calc
#Calculate 3 different tips based of what your dinner bill lowercase

bill = float(input("How much was dinner?"))
# Input must be float as all bills are differnet

tip1 = 0.15
tip2 = 0.20
tip3 = 0.25

print(f"Tip 15 percent which will be {bill * 0.15} for a total of {bill * 0.15 + bill:.2f}")
print(f"Tip 20 percent which will be {bill * 0.20} for a total of {bill * 0.15 + bill:.2f}")
print(f"Tip 25 percent which will be {bill * 0.25 }for a total of {bill * 0.15 + bill:.2f}")
