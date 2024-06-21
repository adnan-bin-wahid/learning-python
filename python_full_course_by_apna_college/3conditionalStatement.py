#if-elif-else
"""
if(conditon):
    statement 1
elif(condition):
    statement 2
else: 
    statement N
"""

# Traffic Lights Code

#light = input("Light : ")
light = "Red"

if(light == "Red"):
    print("Stop")
elif(light == "Yellow"):
    print("Look")
elif(light == "Greed"):
    print("Go")
else:
    print("Light is broken")

# A=5 & G=M
# A=2 & G=F

#A = int(input("A : "))
#G = input("M/F : ")
A=3
G = "M"

if((A == 1 or A==2) and G =="M"):
    print("fee is 100")
elif( A==3 or A==4 or G=="F"):
    print("fee is 200")
elif(A==5 and G == "M"):
    print("Fee is 300")
else:
    print("No fee")    
    
# Ternary operator

# food =input("Food : ")
# eat = "Yes" if food == "cake" else "no"
# print(eat)

food = input("Food :")
# eat = "Yes" if food == "cake" or food == "jalebi" else "no"
# print(eat)

print("Yes") if food == "cake" or food == "jalebi" else print("no")



# Clever IF
#VER= (false_value, true_value)[condition]

age = int(input("Age : "))
vote = ("no","yes")[age>=18]
print(vote)

salary = float(input("Salary : "))
tax = salary *(0.1,0.2)[salary > 50000]
print(tax)