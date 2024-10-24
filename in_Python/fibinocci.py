numb = int(input("Enter the number of terms: "))

# Initialize the first two terms
i, j = 0, 1

# Check for valid input
if numb <= 0:
 print("Invalid number of terms")
else :
 # Print the first term
 print(0)

if numb >= 1:
 # Generate the Fibonacci sequence
 for k in range(2, numb+1 ):
  Ans = i + j
  j = i
  i = Ans
  print(Ans)