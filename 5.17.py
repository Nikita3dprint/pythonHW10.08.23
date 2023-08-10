a = [int(x) for x in open('17var5.txt')]
k = 0
mxraz = -20005
for i in range(len(a)-1):
    if (a[i] % 10 == 5) and (a[i+1] % 10 == 5):
        k += 1
        if abs(a[i] - a[i+1]) > mxraz:
            mxraz = abs(a[i] - a[i+1])
print(k, mxraz)
