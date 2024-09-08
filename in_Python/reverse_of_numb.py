numb = int(input("enter a number:"))
reverse = 0
while numb != 0:
    last_numb = numb % 10
    reverse = reverse * 10 + last_numb
    numb = numb // 10
print("reverse of a given numvber is ", reverse)
