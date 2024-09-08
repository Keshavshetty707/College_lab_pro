input1 = int(input("enter first number: "))
input2 = int(input("enter second number: "))
input3 = int(input("enter three number: "))

if input1 > input2 and input1 > input3:
    print("first number is largest")
elif input2 > input1 and input2 > input3:
    print("second number is largest")
else:
    print("third number is largest")
