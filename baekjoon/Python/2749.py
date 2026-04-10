a, b = 0, 1
for i in range(10000):
    a, b = b, (a+b)%1000000
    print(f"{i+1}: {a}")