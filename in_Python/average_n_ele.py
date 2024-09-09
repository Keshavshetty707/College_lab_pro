Average_list = []
i = 0
Sum = 0
numb = int(input("Enter the number of elements:"))
print("Enter array elements:")
for _ in range(numb):
    Elements = int(input())
    Average_list.append(Elements)
for _ in range(numb):
    Sum = Sum + Average_list[i]
    i += 1
Avg = Sum / numb
print("Average:", Avg)