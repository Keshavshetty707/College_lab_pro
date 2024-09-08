First_array = []
row = int(input("Enter the number of rows:"))
rows = row
col = int(input("Enter the number of cols:"))
print()

print("First Matrix ")
for i in range(row):
    row = []
    for j in range(col):
        element = int(input("Enter element for row {} column {} :".format(i+1, j+1)))
        row.append(element)
    First_array.append(row)

print("First Matrix Output")
for i in First_array:
    for j in i:
        print(j, end=" ")
    print()
print()

print("Second Matrix")
Second_array = []
for i in range(rows):
    row = []
    for j in range(col):
        element = int(input("Enter element for row {} column {} :".format(i+1, j+1)))
        row.append(element)
    Second_array.append(row)

print("Second Matrix Output")
for i in Second_array:
    for j in i:
        print(j, end=" ")
    print()
print()

opr = input("Enter the operator:")

if opr == '+':
    i = 0
    j = 0
    Ans_array = []

    for i in range(rows):
        temp = []
        for j in range(col):
            Ans = First_array[i][j] + Second_array[i][j]
            temp.append(Ans)
        Ans_array.append(temp)

    print("Sum of First and Second Matrix elements Output")
    for i in Ans_array:
        for j in i:
            print(j, end=" ")
        print()

if opr == '-':
    i = 0
    j = 0
    Ans_array = []

    for i in range(rows):
        temp = []
        for j in range(col):
            Ans = First_array[i][j] - Second_array[i][j]
            temp.append(Ans)
        Ans_array.append(temp)

    print("Subtraction of First and Second Matrix elements Output")
    for i in Ans_array:
        for j in i:
            print(j, end=" ")
        print()
