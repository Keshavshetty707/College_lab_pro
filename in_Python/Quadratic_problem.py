A = int(input("enter A value:"))
B = int(input("enter B value:"))
C = int(input("enter C value:"))
root = B*B-4*A*C
if root < 0:
    N = 0
elif root == 0:
    N = 1
else:
    N = 2
match N:
    case 0:
        print("Both roots are imaginary")
    case 1:
        print("Both roots are equal")
        x = B / 2 * A
        print("x=", x)
    case 2:
        print("roots are real and distinct")
        x_plus = - B + (B * B * 4 * A * C)
        x_minus = - B - (B * B * 4 * A * C)
        print("x_plus", x_plus)
        print("x_minus", x_minus)
