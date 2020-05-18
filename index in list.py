l = list(input("Enter some numbers : "))
print(l)
y = str(input("Enter the number : "))
for i in range(len(l)):
    if y == l[i]:
        print(i)

