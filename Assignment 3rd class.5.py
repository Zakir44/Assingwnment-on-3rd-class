lst1 = []
lst2 = []

print("Enter the value for List_1 ")
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst1.append(ele)

print(lst1)

print("Enter the value for List_2 ")
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst2.append(ele)

print(lst2)

Z = set(lst1)
A = set(lst2)

if A.intersection(Z):
    print(" True")
else:
    print("False")

