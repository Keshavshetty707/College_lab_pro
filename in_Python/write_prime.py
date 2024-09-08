numb = int(input("Enter a number:"))

if numb > 1:
    print(2)

for i in range(3, numb+1, 2):
    is_prime = True
    for j in range(2, i, 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

