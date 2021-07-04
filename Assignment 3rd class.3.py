list1 = []


n = int(input("Enter number of elements in list: "))


for i in range(0, n):
    ele = int(input("Enter elements: "))
    list1.append(ele)

    list1.sort()


print("Largest element is:", list1[-1])
