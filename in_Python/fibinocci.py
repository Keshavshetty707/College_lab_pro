numb = int(input("Enter A number"))
j = 0
i = 1
print(j)
print(i)
for _ in range(2, numb):
  Ans = i + j
  j = i
  i = Ans
  print(Ans)
