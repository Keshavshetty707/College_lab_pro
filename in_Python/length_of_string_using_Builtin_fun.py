import sys
name = input("Enter a String:")
char = name
char_size = sys.getsizeof(char)
Ans = char_size - 41
print(Ans)

