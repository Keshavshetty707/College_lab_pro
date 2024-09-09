numb1 = int(input("enter any two numbers:"))
numb2 = int(input())
if numb1 < numb2:
    temp = numb1
    numb1 = numb2
    numb2 = temp
rem = 1
k = 1
Ans = 0
while rem != 0:
    if k == 1:
        rem = 0
    k += 1
    rem = numb1 % numb2
    if rem != 0:
        Ans = rem
    numb1 = numb2
    numb2 = rem
print(Ans)
