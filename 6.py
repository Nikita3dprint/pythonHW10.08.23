for x in range(71):
    s = x * '1'
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    print(s)
