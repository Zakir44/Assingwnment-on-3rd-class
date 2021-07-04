list1 = []
count = 0


n = int(input("Enter number of elements in list: "))


for i in range(0, n):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print(list1)
Z = int(input("Enter number of element wants to search in list: "))
for i in range(0, len(list1)):
    if Z == list1[i]:
        count = count + 1
    print(count)
