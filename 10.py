for x in range(201, 1000):
    s = '5' * x
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '555', 1)
    print(x, s.count('5'))

