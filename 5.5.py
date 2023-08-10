for n in range(200):
    n = n - n % 4
    b = bin(n)[2:]
    b = b + str(b.count('1') % 2)
    r = int(b, 2)
    if r > 56:
        print(r)
        break
