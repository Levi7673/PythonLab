# Python program to read list of names and sort the list in alphabetical order.

names = []
n = int(input("Enter how many names : "))
for i in range (n):
    names.append(input("Enter name :"))
print("Names : ", names)
names.sort()
print("Names in sorted order : ", names) 

# Enter how many names : 3
# Enter name :Ponni
# Enter name :Thatha
# Enter name :Anandhu
# Names :  ['Ponni', 'Thatha', 'Anandhu']
# Names in sorted order :  ['Anandhu', 'Ponni', 'Thatha']