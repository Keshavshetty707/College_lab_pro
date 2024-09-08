numb = int(input("Enter a number:"))
flag = 0
if numb == 1:
    print(numb, "is not a prime number")
elif numb == 2:
    print(numb, "is a prime number")

if numb > 2:
    for i in range(2, numb, 1):
        if numb % i == 0:
            flag = 1
            break

    if flag == 0:
        print(numb, "is a prime number")
    else:
        print(numb, "is not a prime number")
