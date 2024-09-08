numb = int(input("enter a number:"))
original_value = numb
reverse = 0

while numb != 0:
    last_numb = numb % 10
    reverse = reverse * 10 + last_numb
    numb = numb // 10
if reverse == original_value:
    print("given number is a palindrome")
else:
    print("given number is not a palindrome")
