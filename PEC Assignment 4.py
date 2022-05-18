''' Assignment 4
Anirudh Ralhan, bt21107091'''

from random import randint

# Question 1

print("Question 1")

marks = float(input("Enter your marks : "))
if marks > 80:
    print("Your grade is A.")
elif marks > 60:
    print("Your grade is B.")
elif marks > 50:
    print("Your grade is C.")
elif marks > 45:
    print("Your grade is D.")
elif marks > 25:
    print("Your grade is E.")
elif marks >= 0:
    print("Your grade is F.")
    
print("----------------------------------------------------")
    
# Question 2

print("Question 2")

year = int(input("Enter year : "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

print("----------------------------------------------------")
# Question 3

print("Question 3")

for i in range(10):
    num1 = randint(0,10)
    num2 = randint(0,10)
    trueans = num1 * num2
    print("Q.",i+1," : ",num1," x ",num2)
    userans = int(input("Enter your answer : "))
    if userans == trueans:
        print("Right!\n")
    else:
        print("Wrong. The answer is ",trueans,"\n")

print("----------------------------------------------------")
# Question 4

print("Question 4")

for i in range(200):
    if i % 5 != 2:
        continue
    if i % 6 != 3:
        continue
    if i % 7 != 2:
        continue
    print(i," is the possible value of number of candies.")