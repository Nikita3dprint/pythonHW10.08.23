for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(not x or y)) or (not z) or w == 0:
                    print(x, y, z, w)

#1 0 0 0
#1 0 0 1
#1 0 1 0
#1 0 1 1
#1 1 0 0
#1 1 0 1
#1 1 1 0