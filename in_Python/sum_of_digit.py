numb = int(input("enter a number:"))
Ans = 0
while numb != 0:
    last_num = numb % 10
    Ans = Ans + last_num
    numb = numb // 10
print("Sum of given number is :", Ans)
