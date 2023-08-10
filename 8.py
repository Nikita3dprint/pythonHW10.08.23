for x in range(201, 1000):
    s = '5' * x
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    if s.count('8') > s.count('5'):
        print(x)
        break
