N = int(input('chislo'))
i = 0
while N >= 2**i:
    i += 1
    print(2**(i-1), end=' ')