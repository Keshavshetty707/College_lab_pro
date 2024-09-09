name = input("enter a string:")
i = 0
Ans = ""
for i in range(0, 1000, 1):
    if i == 0:
        Ans = name[i]
    if i > 0:
        Ans = Ans + name[i]

    if Ans == name:
        break
print(i + 1)
