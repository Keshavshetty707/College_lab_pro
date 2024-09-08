
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

i = 0
j = 0
sum = 0
for i in range(rows):
    for j in range(col):
        if j == i:
            sum += First_array[i][j]
print("Sum=", sum)
