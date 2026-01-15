# Program to find sum of all even no's in a group of 'n' no's entered by the user.

numbers = []
sum = 0
n = int(input("Enter how many no's : "))
for i in range (n):
    numbers.append(int(input("enter no : ")))
print("Numbers : ", numbers)

for i in numbers:
    if i%2 == 0:
        sum = sum+i
print("Sum of even no's : ", sum)


# Enter how many no's : 3
# enter no : 2
# enter no : 3
# enter no : 3
# Numbers :  [2, 3, 3]
# Sum of even no's :  2