sum = 0
for i in range(1001):
    temp = i
    sum = 0 
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        
    if i == sum:
        print(i)
