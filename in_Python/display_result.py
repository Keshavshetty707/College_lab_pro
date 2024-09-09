result = float(input("enter your Exam result(in Percentage):"))
if result < 35.0:
    print("Fail")
elif 45.0 < result < 65.0:
    print("B+")
elif 65.0 < result < 85.0:
    print("A")
elif 85.0 <= result <= 90.0:
    print("A+")
elif 91.0 <= result <= 100:
    print("O+")
else:
    print("invalid input")
