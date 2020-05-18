print("Let the complex number be in format : a+ib")
a = int(input("Enter the a part of the complex number : "))
b = int(input("Enter the b part of the complex number : "))
if a > b:
    print("{} the real part is the greatest".format(a))
else:
    print("{} the imaginary part is the greatest".format(b))

