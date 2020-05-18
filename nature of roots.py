print("Let the quadratic equation be of format : ax²+bx+c")
a = int(input("Enter 'a' from the quadratic equation : "))
b = int(input("Enter 'b' from the quadratic equation : "))
c = int(input("Enter 'c' from the quadratic equation : "))
D = (b*b)-4*a*c
if D == 0:
    print("The roots are equal and real !")
elif D < 0:
    print("The roots are imaginary !")
else:
    print("The roots are real and distinct !")

